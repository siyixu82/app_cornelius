from django.contrib import admin
from cornelius_app import models


admin.site.register(models.CorneliusUser)
admin.site.register(models.Doctor)
admin.site.register(models.Facility)
admin.site.register(models.Patient)
admin.site.register(models.MeetingScript)
admin.site.register(models.VisitJournal)
admin.site.register(models.MeetingInfo)
#admin.site.register(models.DoctorPatientMeeting)

# Register your models here.
