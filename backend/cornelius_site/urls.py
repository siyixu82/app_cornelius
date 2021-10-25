"""cornelius_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from cornelius_app import views
from django.urls import path,include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


#from django.conf.urls import url
#from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'visit_journal', views.VisitJournalSet)
#router.register(r'meetingInfo', views.MeetingInfoSet)

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include(router.urls)),
  path("meeting/pid<int:pk>/", views.MeetingInfoByPid.as_view()),
  path("user/uid<int:pk>/", views.UserInfoByUid.as_view()),
  path("login/", views.LogIn.as_view()),
  path("signup/", views.SignUp.as_view()),
  path("meeting/mid<int:pk>/", views.MeetingScriptByMid.as_view()),
  path("facility/uid<int:pk>/",views.FacilityByUid.as_view()),
  path("doctor/uid<int:pk>/",views.DoctorByUid.as_view()),
  path("meeting/",views.NewMeeting.as_view()),
]
