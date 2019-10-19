from rest_framework import serializers

class CardStatSerializer(serializers.Serializer):
  allUser = serializers.IntegerField()
  newUser = serializers.IntegerField()
  lesson = serializers.IntegerField()