from django.urls import path

from .views import JenkinsView, JenkinsBuildView

app_name = 'jenkin'

urlpatterns = [
  path(r'', JenkinsView.as_view()),
  path(r'build/', JenkinsBuildView.as_view())
]