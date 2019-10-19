from django.db.models import Count, Max
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime, timedelta

from .serialiers import CardStatSerializer
from user.models import User
from lessons.models import Learning

class CardStatView(APIView):
  def get(self, request):
    allUser = User.objects.count()
    lastWeek = datetime.today() - timedelta(days=7)
    newUser = User.objects.filter(createdAt__gte=lastWeek).count()
    groups = {}
    learnedUser = Learning.objects.values('user').distinct()
    for user in learnedUser:
      lastLesson = Learning.objects.filter(user=user['user']).values('lesson__lessonGroup').last()
      key = str(lastLesson['lesson__lessonGroup'])
      try:
        groups[key] = groups[key] + 1
      except KeyError:
        groups[key] = 1
    mostGroups = max(groups, key=groups.get)
    data = {
      'allUser': allUser,
      'newUser': newUser,
      'lesson': mostGroups,
    }
    result = CardStatSerializer(data, many=False).data
    return Response(result)
