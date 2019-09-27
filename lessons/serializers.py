from rest_framework import serializers

from .models import LessonGroup, Lesson, Learning

class LessonGroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = LessonGroup
    fields = ('id', 'name')

class LessonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lesson
    fields = ('id', 'topic', 'description', 'lessonGroup', 'addedBy')

class LearningSerializer(serializers.ModelSerializer):
  class Meta:
    model = Learning
    fields = ('user', 'lesson')
