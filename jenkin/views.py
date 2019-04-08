from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

from .jenkinsClient import JenkinsClient
from .serializers import JenkinsResultSerializer

class JenkinsView(APIView):
  __jenkinsClient = None
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.__jenkinsClient = JenkinsClient()

  def post(self, request):
    result = None
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    jobName = body['jobName']
    self.__jenkinsClient.createJob(jobName)
    self.__jenkinsClient.buildJob(jobName)
    data = {
      'result': True
    }
    result = JenkinsResultSerializer(data, many=True).data
    return Response(result)
