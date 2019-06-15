from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from rest_framework_jwt.utils import jwt_decode_handler

class VerifyJwtMiddleware(MiddlewareMixin):
  def __unauthorized(self):
    return HttpResponse({'Unauthorized'}, status=401)
  
  def process_request(self, request):
    if 'fb-login/' not in request.path:
      if 'HTTP_AUTHORIZATION' not in request.META.keys():
        return self.__unauthorized()
      authorization = request.META['HTTP_AUTHORIZATION']
      token = authorization.replace('Bearer ', '')
      try:
        jwt_decode_handler(token)
      except:
        return self.__unauthorized()

    