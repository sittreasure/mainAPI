import json
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.utils import jwt_encode_handler

from base.jwt import jwt_payload_handler
from .models import User
from .serializers import UserSerializer

class UserViewSet(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAuthenticated]

class FacebookAuthView(APIView):
  permission_classes = []

  def get(self, request):
    return Response({
      'msg': 'hello'
    })

  def post(self, request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    fbId = body['fbId']

    user = None
    try:
      user = User.objects.get(id=fbId)
    except User.DoesNotExist:
      fbName = body['fbName']
      fbSurname = body['fbSurname']
      fbImg = body['fbImg']
      user = User.objects.create(id=fbId, name=fbName, surname=fbSurname, avatar=fbImg)
    
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)

    return Response({
      'accessToken': token,
    })
