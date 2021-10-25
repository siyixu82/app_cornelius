from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import viewsets
from cornelius_app.models import *
from cornelius_app.serializers import *
from django.db.utils import IntegrityError
from django.forms.models import model_to_dict
import json
from rest_framework import status
from cornelius_app.transcribe_async import transcribe_gcs, upload_to_bucket, transcribe_file
from django.core.files.storage import FileSystemStorage


class UserViewSet(viewsets.ModelViewSet):

    queryset = CorneliusUser.objects.all()
    serializer_class = UserSerializer


class MeetingInfoSet(viewsets.ModelViewSet):

    queryset = MeetingInfo.objects.all()
    serializer_class = MeetingInfoSerializer


class VisitJournalSet(viewsets.ModelViewSet):

    queryset = VisitJournal.objects.all()
    serializer_class = VisitJournalSerializer


def search_name(id):
    person = model_to_dict(CorneliusUser.objects.get(uid=id))
    return(person['first_name'] + " " + person['last_name'])


def search_facility(id):
    facility = model_to_dict(Facility.objects.get(fid=id))
    return(facility['name'])


def search_facility_addr(id):
    facility = model_to_dict(Facility.objects.get(fid=id))
    return(facility['address'])


def search_email(id):
    person = model_to_dict(CorneliusUser.objects.get(uid=id))
    return(person['email'])


class MeetingInfoByPid(APIView):

    def get_object(self, pk):
        try:
            return MeetingInfo.objects.filter(pid=pk)
        except MeetingInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):

        meeting_list = list(self.get_object(pk).values())

        for meeting in meeting_list:
            name = search_name(meeting['did_id'])
            facility = search_facility(meeting['fid_id'])
            mid = meeting['mid']
            try:
                script = model_to_dict(MeetingScript.objects.get(mid=mid))
                meeting['script'] = script['script']
            except MeetingScript.DoesNotExist:
                meeting['script'] = "meeting script not available"

            meeting['Doctor'] = name
            meeting['Facility'] = facility

        return JsonResponse(meeting_list, safe=False)
# Example Request Body:
# {
#     "email":"sx53@duke.edu",
#     "password":"123456"
# }


class LogIn(APIView):

    def post(self, request, format=None):
        request_dict = json.loads(request.body)
        print('yes')
        print(request_dict)
        email = request_dict.get("email")
        password = request_dict.get("password")

        try:
            user = model_to_dict(CorneliusUser.objects.get(email=email))
            if(user['password'] == password):
                return JsonResponse({"uid": user['uid'], "role": user['role']}, status=status.HTTP_200_OK, safe=False)
            else:
                return JsonResponse({"detail": "Password incorret"},
                                    status=status.HTTP_401_UNAUTHORIZED, safe=False)
        except CorneliusUser.DoesNotExist:
            return JsonResponse({"detail": "Cannot find this user"},
                                status=status.HTTP_400_BAD_REQUEST, safe=False)


class SignUp(APIView):

    def post(self, request, format=None):

        request_dict = json.loads(request.body)
        first = request_dict.get("first_name")
        last = request_dict.get("last_name")
        email = request_dict.get("email")
        password = request_dict.get("password")
        role = request_dict.get("role")

        try:
            user = CorneliusUser(first_name=first,
                                 last_name=last,
                                 email=email,
                                 password=password,
                                 role=role
                                 )
            user.save()
        except IntegrityError:  # double check
            return JsonResponse({"detail": "Email alreadly sign up"},
                                status=status.HTTP_400_BAD_REQUEST, safe=False)

        user = model_to_dict(CorneliusUser.objects.get(email=email))
        return JsonResponse({"uid": user['uid']}, status=status.HTTP_200_OK, safe=False)


class NewMeeting(APIView):

    def post(self, request, format=None):

        request_dict = json.loads(request.body)
        pid = request_dict.get("pid")
        patient = Patient.objects.get(pid=pid)

        did = request_dict.get("did")
        doctor = Doctor.objects.get(did=did)
        # print(doctor)

        fid = request_dict.get("fid")
        facility = Facility.objects.get(fid=fid)

        date = request_dict.get("date")
        reason = request_dict.get("reason")

        try:
            meeting = MeetingInfo(
                pid=patient,
                did=doctor,
                fid=facility,
                date=date,
                reason=reason
            )
            meeting.save()
            return JsonResponse({"mid": model_to_dict(meeting)['mid']}, status=status.HTTP_200_OK, safe=False)
        except IntegrityError:
            return JsonResponse({"detail": "Cannot create new meeting"},
                                status=status.HTTP_400_BAD_REQUEST, safe=False)

        return JsonResponse([], status=status.HTTP_200_OK, safe=False)

# {
#      "name":"Duke Hospital",
#      "address":"3611 University Drive"
# }


class FacilityByUid(APIView):

    def get(self, request, pk, format=None):
        try:
            facility_list = MeetingInfo.objects.filter(
                pid=pk).order_by("fid").values("fid").distinct()

            for facility in facility_list:
                facility['name'] = search_facility(facility['fid'])
                facility['address'] = search_facility_addr(facility['fid'])

            return JsonResponse({'data': list(facility_list)}, status=status.HTTP_200_OK, safe=False)
        except MeetingInfo.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        request_dict = json.loads(request.body)
        name = request_dict.get("name")
        address = request_dict.get("address")
        facility = None
        if(Facility.objects.filter(name=name).exists()):
            facility = Facility.objects.get(name=name)
        else:
            facility = Facility(name=name, address=address)
            facility.save()

        data = FacilitySerializer(facility).data
        return JsonResponse(data, status=status.HTTP_200_OK, safe=False)


class DoctorByUid(APIView):

    def get(self, request, pk, format=None):
        try:
            doctor_list = MeetingInfo.objects.filter(
                pid=pk).order_by("did").values("did").distinct()

            for doctor in doctor_list:
                doctor['name'] = search_name(doctor['did'])
                doctor['email'] = search_email(doctor["did"])

            return JsonResponse({'data': list(doctor_list)}, status=status.HTTP_200_OK, safe=False)
        except MeetingInfo.DoesNotExist:
            raise Http404

# {
#      "first_name":"Duke",
# "last_name":"Hospital",
# "email": "Duke@Hospital.com "
# }

    def post(self, request, pk, format=None):

        request_dict = json.loads(request.body)
        first = request_dict.get("first_name")
        last = request_dict.get("last_name")
        email = request_dict.get("email")
        doctor = None

        if(CorneliusUser.objects.filter(email=email).exists() and CorneliusUser.objects.get(email=email).role == "D"):
            doctor = CorneliusUser.objects.get(email=email)
        else:
            doctor = CorneliusUser(first_name=first,
                                   last_name=last,
                                   email=email,
                                   password=123456,
                                   role="D"
                                   )
            doctor.save()

        data = UserSerializer(doctor).data
        return JsonResponse(data, status=status.HTTP_200_OK, safe=False)


class UserInfoByUid(APIView):

    def get_object(self, pk):
        try:
            return CorneliusUser.objects.get(uid=pk)
        except CorneliusUser.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        # print(pk)
        request_dict = json.loads(request.body)
        user = self.get_object(pk)

        address = request_dict.get("address")
        insurance = request_dict.get("insurance")
        first = request_dict.get("first_name")
        last = request_dict.get("last_name")
        role = request_dict.get("role")

        try:
            if(first):
                user.first_name = first
            if(last):
                user.last_name = last
            user.save()
        except IntegrityError:
            return JsonResponse({"detail": "Cannot Update the Infomation"},
                                status=status.HTTP_400_BAD_REQUEST, safe=False)
        try:
            if(role == "P" and address):
                patient = Patient.objects.get(pid=pk)
                patient.address = address
                patient.save()
            if(role == "P" and insurance):
                patient = Patient.objects.get(pid=pk)
                patient.insurance = insurance
                patient.save()
        except Patient.DoesNotExist:
            raise Http404

        return self.get(request, pk)

    def get(self, request, pk, format=None):
        person = model_to_dict(self.get_object(pk))

        del person['password']
        person['detail'] = {}

        if person['role'] == 'D':
            try:
                doctor = model_to_dict(Doctor.objects.get(did=pk))
                fid = doctor['fid']
                person['detail'] = doctor
                person['detail']['facility'] = search_facility(fid)
            except Doctor.DoesNotExist:
                raise Http404

        if person['role'] == 'P':
            try:
                person['meeting'] = {'name': {}, 'facility': {}}
                patient = model_to_dict(Patient.objects.get(pid=pk))
                person['detail'] = patient
                doctor_list = MeetingInfo.objects.filter(
                    pid=pk).values("did").distinct()
                print(doctor_list)

                for doctor in doctor_list:
                    did = doctor['did']
                    fid = model_to_dict(Doctor.objects.get(did=did))['fid']
                    person['meeting']['name'] = search_name(did)
                    person['meeting']['facility'] = search_facility(fid)
            except Patient.DoesNotExist:
                raise Http404
        return JsonResponse(person, safe=False, status=status.HTTP_200_OK,)


class MeetingScriptByMid(APIView):

    def post(self, request, pk, format=None):
        myfile = request.FILES['file']
        blob_public_url = upload_to_bucket(
            'helloWorld', myfile.file, 'visit_recordings')
        try:
            # create instance of class/model and call save()
            meeting_script = MeetingScript(
                mid=MeetingInfo.objects.get(mid=pk),
                script=transcribe_gcs(blob_public_url)
            )
            # post to database
            meeting_script.save()
        except IntegrityError:  # double check
            return JsonResponse({"detail": "Failed to save script"},
                                status=status.HTTP_400_BAD_REQUEST, safe=False)
        # generate visit journal and store it
        # store in database under the same meeting id "create script succesfully"
        return JsonResponse({"detail": meeting_script.script}, status=status.HTTP_200_OK, safe=False)

    def get(self, request, pk, format=None):
        try:
            meeting_script = MeetingScript.objects.get(mid=pk)
            data = MeetingScriptSerializer(meeting_script).data
            return JsonResponse(data, safe=False)
        except MeetingScript.DoesNotExist:
            raise Http404
