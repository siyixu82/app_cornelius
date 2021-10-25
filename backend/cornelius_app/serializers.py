from cornelius_app.models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorneliusUser
        fields = ['uid', 'first_name', 'last_name','role','email']


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class MeetingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingInfo
        fields = '__all__'

class VisitJournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitJournal
        fields = '__all__'

class MeetingScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingScript
        fields = '__all__'