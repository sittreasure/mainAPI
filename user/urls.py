from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, FacebookAuthView, MeView

router = routers.DefaultRouter()

router.register(r'', UserViewSet)

urlpatterns = [
  path(r'me/', MeView.as_view()),
  path(r'fb-login/', FacebookAuthView.as_view()),
  path(r'', include(router.urls))
]
