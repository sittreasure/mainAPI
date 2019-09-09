from django.urls import path, include
from rest_framework import routers

from .views import LessonGroupViewSet, LessonViewSet, LearningViewSet

router = routers.DefaultRouter()

router.register(r'group', LessonGroupViewSet)
router.register(r'learning', LearningViewSet, basename='LearningModel')
router.register(r'', LessonViewSet)

urlpatterns = [
  path(r'', include(router.urls))
]
