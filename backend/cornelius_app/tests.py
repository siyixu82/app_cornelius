from django.test import TestCase
from cornelius_app.models import *
import json
#sfrom django.core.urlresolvers import reverse

#from django.test.client import Client
# Create your tests here.

class URLTests(TestCase):

	def test_timeline (self):
		response = self.client.get("/meeting/pid1/")
		self.assertEqual(response.status_code,200)

	def test_facility (self):
		response = self.client.get("/facility/uid1/")
		self.assertEqual(response.status_code,200)

	def test_doctor(self):
		response = self.client.get("/doctor/uid1/")
		self.assertEqual(response.status_code,200)


class UserTestCase(TestCase):
	@classmethod
	def setUpTestData(cls):
		CorneliusUser.objects.create(first_name="patient", 
			last_name = "test",role = "P",
			email = "patient@test.com",password = "123456")
		CorneliusUser.objects.create(first_name="doctor", 
			last_name = "test",role = "D",
			email = "doctor@test.com",password = "123456")

		Facility.objects.create(name = "Duke Hospital",address = "3611 University Drive")

		MeetingInfo.objects.create(
			pid = Patient.objects.get(pid = 1),
			did = Doctor.objects.get(did = 2),
			fid = Facility.objects.get(fid = 1),
			date = "2020-10-22",reason = "testing reason")

		MeetingScript.objects.create(
			mid = MeetingInfo.objects.get(mid = 1),
			script = "Testing Script"
		)

		MeetingInfo.objects.create(
			pid = Patient.objects.get(pid = 1),
			did = Doctor.objects.get(did = 2),
			fid = Facility.objects.get(fid = 1),
			date = "2020-10-22",reason = "testing reason")
	

	def test_user_name(self):
		first_name = CorneliusUser.objects.get(uid = 1).first_name
		last_name = CorneliusUser.objects.get(uid = 1).last_name
		self.assertEqual(first_name, "patient")
		self.assertEqual(last_name, "test")

	def test_patient_exist(self):
		
		pid = CorneliusUser.objects.get(email = "patient@test.com").uid
		patient = Patient.objects.filter(pid = pid)
		self.assertEqual(patient.exists(), True)

	def test_doctor_exist(self):
		
		did = CorneliusUser.objects.get(email = "doctor@test.com").uid
		doctor = Doctor.objects.filter(did = did)
		self.assertEqual(doctor.exists(), True)

	def test_patientinfo_url(self):
		
		response = self.client.get("/user/uid1/")
		self.assertEqual(response.status_code,200)

	def test_doctorinfo_url(self):
		doctor = Doctor.objects.get(did = 2)
		doctor.fid = Facility.objects.get(fid = 1)
		doctor.save()
		response = self.client.get("/user/uid2/")
		self.assertEqual(response.status_code,200)

	def test_facility_name(self):
		name = Facility.objects.get(fid = 1).name
		self.assertEqual(name, "Duke Hospital")

	def test_facility_address(self):
		address = Facility.objects.get(fid = 1).address
		self.assertEqual(address, "3611 University Drive")

	def test_meeting_reason(self):
		reason = MeetingInfo.objects.get(mid = 1).reason
		self.assertEqual(reason, "testing reason")

	def test_meeting_script_db(self):
		print(MeetingScript.objects.all())
		script = MeetingScript.objects.get(mid = 1).script
		self.assertEqual(script, "Testing Script")

	def test_meeting_script_api(self):
		response = self.client.get("/meeting/mid1/")
		self.assertEqual(response.status_code,200)

	def test_meeting_script_api_json(self):
		response = self.client.get("/meeting/mid1/")
		script = json.loads(response.content)['script']
		self.assertEqual(script,"Testing Script")

	def test_userinfo_negative(self):
		response = self.client.get("user/uid3/")
		self.assertEqual(response.status_code,404)

	def test_meetinginfo_negative(self):
		response = self.client.get("/meeting/pid1/")
		script1 = json.loads(response.content)[0]['script']
		script2 = json.loads(response.content)[1]['script']
		self.assertEqual(script1,"Testing Script")
		self.assertEqual(script2,"meeting script not available")

	def test_post_login(self):
		
		request = {"email":"patient@test.com","password":"123456"}
		response = self.client.post("/login/",json.dumps(request),
                                content_type="application/json")
		self.assertEqual(response.status_code, 200)

	def test_post_login_negative(self):
		
		request = {"email":"patient@test.com","password":"12345"}
		response = self.client.post("/login/",json.dumps(request),
                                content_type="application/json")
		self.assertEqual(response.status_code, 401)

	def test_post_signup(self):
		request = {
			"first_name": "Siyi",
			"last_name" :"Xu10",
			"email":"xusiyi10@gmail",
			"password":"123456",
			"role": "P"
		}
		response = self.client.post("/signup/",json.dumps(request),
                                content_type="application/json")
		self.assertEqual(response.status_code, 200)

	def test_post_signup_negative(self):
		request = {
			"first_name": "Siyi",
			"last_name" :"Test",
			"email":"patient@test.com",
			"password":"123456",
			"role": "P"
		}
		response = self.client.post("/signup/",json.dumps(request),
                                content_type="application/json")
		self.assertEqual(response.status_code, 400)

	def test_post_facility(self):
		request = {
		    "name":"Duke Hospital",
		    "address":"3611 University Drive"
		}

		response = self.client.post("/facility/uid1/",json.dumps(request),
                                content_type="application/json")
		self.assertEqual(response.status_code, 200)

	def test_post_doctor(self):
		request = {
		    "first_name":"Duke",
		    "last_name":"Hospital",
		    "email": "Duke@Hospital.com "
		}

		response = self.client.post("/doctor/uid1/",json.dumps(request),
                                content_type="application/json")
		self.assertEqual(response.status_code, 200)

	def test_post_meeting(self):
		request = {
		     "pid":"1",
		     "did":"2",
		     "fid":"1",
		     "date":"2020-10-22",
		     "reason":"test endpoint"
		}

		response = self.client.post("/meeting/",json.dumps(request),
                                content_type="application/json")
		self.assertEqual(response.status_code, 200)






	