from rest_framework import viewsets

from .models import LessonGroup, Lesson, Learning
from .serializers import LessonGroupSerializer, LessonSerializer, LearningSerializer
from base.jwt import getUserId

class LessonGroupViewSet(viewsets.ModelViewSet):
  queryset = LessonGroup.objects.all()
  serializer_class = LessonGroupSerializer

class LessonViewSet(viewsets.ModelViewSet):
  queryset = Lesson.objects.all()
  serializer_class = LessonSerializer

class LearningViewSet(viewsets.ModelViewSet):
  queryset = Learning.objects.all()
  serializer_class = LearningSerializer
  def get_queryset(self):
    queryset = self.queryset
    userId = getUserId(self.request)
    return queryset.filter(user=userId)
