from django.conf import settings
from jenkins import Jenkins

class JenkinsClient:
  __jenkin = None

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    url = getattr(settings, 'JENKINS_URL')
    username = getattr(settings, 'JENKINS_USERNAME')
    password = getattr(settings, 'JENKINS_PASSWORD')
    self.__jenkin = Jenkins(url, username=username, password=password)
  