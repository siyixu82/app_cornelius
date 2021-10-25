from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save


ROLE_TYPE= (
    ('P', 'Patient'),
    ('D', 'Doctor'),
)

class CorneliusUser(models.Model):
	uid =  models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	role = models.CharField(max_length=10, choices = ROLE_TYPE)
	email = models.EmailField(max_length=254,unique = True)
	password = models.CharField(max_length=30)
	#created = models.DateTimeField(auto_now_add=True)

	class Meta:
		#ordering = ['created']
		db_table = 'cornelius_user'


class Doctor(models.Model):
	did = models.OneToOneField('CorneliusUser',on_delete=models.CASCADE,primary_key=True,db_column='uid')
	fid = models.ForeignKey('Facility', on_delete= models.DO_NOTHING,db_column='fid',null=True,blank = True)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True,blank = True) # validators should be a list
	
	# class Meta:
	# 	#ordering = ['created']
	# 	db_table = 'doctor'

class Patient(models.Model):
	pid = models.OneToOneField('CorneliusUser',on_delete=models.CASCADE,primary_key=True,db_column='uid')
	address = models.CharField(max_length=50,null=True,blank = True)
	insurance = models.CharField(max_length=50,null=True,blank = True)

	# class Meta:
	# 	#ordering = ['created']
	# 	db_table = 'patient'

def create_doctor(sender,instance,created, **kwargs):
	if created:
		if(instance.role == "D"):
			Doctor.objects.create(did = instance)

def create_patient(sender,instance,created, **kwargs):
	if created:
		if(instance.role == "P"):
			Patient.objects.create(pid = instance)
		

post_save.connect(create_patient,sender = CorneliusUser)
post_save.connect(create_doctor,sender = CorneliusUser)


class Facility(models.Model):
	fid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)

	class Meta:
		db_table = 'facility'

# class DoctorPatientMeeting(models.Model):
# 	pid = models.ForeignKey('Patient', on_delete= models.DO_NOTHING,db_column='pid')
# 	did = models.ForeignKey('Doctor', on_delete= models.DO_NOTHING,db_column='did')
# 	date = models.DateField()

# 	class Meta:
# 		db_table = 'doctor_patient_meeting'

class MeetingInfo(models.Model):
	mid = models.AutoField(primary_key=True)
	pid = models.ForeignKey('Patient', on_delete= models.DO_NOTHING,db_column='pid')
	did = models.ForeignKey('Doctor', on_delete= models.DO_NOTHING,db_column='did')
	fid = models.ForeignKey('Facility', on_delete= models.DO_NOTHING,db_column='fid')
	date = models.DateField()
	reason = models.TextField()

	class Meta:
		ordering = ['date']
		db_table = 'meeting_info'

def update_faciliy(sender,instance,created, **kwargs):
	if created:
		#print(instance)
		doctor = Doctor.objects.get(did = instance.did)
		#print(doctor.fid)
		doctor.fid = instance.fid
		doctor.save()
			
post_save.connect(update_faciliy,sender = MeetingInfo)

class MeetingScript(models.Model):
	mid = models.ForeignKey('MeetingInfo', on_delete= models.DO_NOTHING,db_column='mid',primary_key=True)
	script = models.TextField()

	class Meta:
		db_table = 'meeting_script'

class VisitJournal(models.Model):
	
	mid = models.ForeignKey('MeetingInfo', on_delete= models.DO_NOTHING,db_column='mid',primary_key=True)
	date = models.DateField()

	treatment = models.TextField()
	diagonisis = models.TextField()
	follow_up = models.TextField()
	question = models.TextField()
	medication = models.TextField()
	notes = models.TextField()
	cost = models.TextField()


	class Meta:
		db_table = 'visit_journal'