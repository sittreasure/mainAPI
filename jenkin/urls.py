from django.urls import path

from .views import JenkinsView

app_name = 'jenkin'

urlpatterns = [
  path(r'', JenkinsView.as_view())
]