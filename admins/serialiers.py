from rest_framework import serializers

class CardStatSerializer(serializers.Serializer):
  allUser = serializers.IntegerField()
  newUser = serializers.IntegerField()
  lesson = serializers.IntegerField()

class ChartStatSerializer(serializers.Serializer):
  count = serializers.IntegerField()
  data = serializers.DictField()

class UserStatSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  name = serializers.CharField()
  avatar = serializers.CharField()
  isAdmin = serializers.BooleanField()
  lesson = serializers.IntegerField(allow_null=True)
