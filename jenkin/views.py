from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
import json

from .jenkinsClient import JenkinsClient
from .serializers import JenkinsResultSerializer, JenkinsLogSerializer
from base.jwt import getUserId

class JenkinsView(APIView):
  __jenkinsClient = None
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.__jenkinsClient = JenkinsClient()

  def post(self, request):
    userId = getUserId(request)
    bucket = str(userId)
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    jobName = body['jobName']
    folder = body['folder']
    self.__jenkinsClient.createJob(jobName, bucket, folder)
    self.__jenkinsClient.buildJob(jobName)
    data = {
      'result': True
    }
    result = JenkinsResultSerializer(data, many=False).data
    return Response(result)

class JenkinsBuildView(APIView):
  __jenkinsClient = None
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.__jenkinsClient = JenkinsClient()
  
  def get(self, request):
    jobName = request.GET.get('job_name', '')
    info = self.__jenkinsClient.getBuildInfo(jobName)
    data = {
      'result': info['building']
    }
    result = JenkinsResultSerializer(data, many=False).data
    return Response(result)

class JenkinsLogView(APIView):
  __jenkinsClient = None
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.__jenkinsClient = JenkinsClient()

  def get(self, request):
    jobName = request.GET.get('job_name', '')
    log = self.__jenkinsClient.getConsoleLog(jobName)
    data = {
      'log': log
    }
    result = JenkinsLogSerializer(data, many=False).data
    return Response(result)
