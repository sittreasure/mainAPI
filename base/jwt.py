from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import jwt_decode_handler
from calendar import timegm
from datetime import datetime

def jwt_payload_handler(user):
  payload = {
    'user_id': user.id,
    'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
  }
  if api_settings.JWT_ALLOW_REFRESH:
    payload['orig_iat'] = timegm(
        datetime.utcnow().utctimetuple()
    )

  return payload

def getUserId(request):
  authorization = request.META['HTTP_AUTHORIZATION']
  token = authorization.replace('Bearer ', '')
  token = jwt_decode_handler(token)
  userId = token['user_id']
  return userId