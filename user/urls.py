from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, FacebookAuthView

router = routers.DefaultRouter()

router.register(r'', UserViewSet)

urlpatterns = [
  path(r'fb-login/', FacebookAuthView.as_view()),
  path(r'', include(router.urls))
]
