from django.urls import path

from .views import JenkinsView, JenkinsBuildView, JenkinsLogView

app_name = 'jenkin'

urlpatterns = [
  path(r'', JenkinsView.as_view()),
  path(r'build/', JenkinsBuildView.as_view()),
  path(r'log/', JenkinsLogView.as_view())
]
