from rest_framework import serializers

class JenkinsResultSerializer(serializers.Serializer):
  result = serializers.BooleanField()
