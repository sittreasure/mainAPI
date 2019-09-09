from django.db import models
from base.models import Timestamp

class LessonGroup(Timestamp):
  name = models.CharField(max_length=100)

  class Meta:
    db_table = 'LessonGroups'

  def __str__(self):
    return 'lesson group : {name}'.format(name=self.name)

class Lesson(Timestamp):
  topic = models.CharField(max_length=100)
  description = models.TextField()
  lessonGroup = models.ForeignKey('lessons.LessonGroup', on_delete=models.CASCADE, db_column='lesson_group_id',)
  addedBy = models.ForeignKey('user.User', on_delete=models.CASCADE, db_column='added_by',)

  class Meta:
    db_table = 'Lessons'

  def __str__(self):
    return 'lesson : {topic}'.format(topic=self.topic)

class Learning(Timestamp):
  user = models.ForeignKey('user.User', on_delete=models.CASCADE)
  lesson = models.ForeignKey('lessons.Lesson', on_delete=models.CASCADE, null=True, blank=True)

  class Meta:
    db_table = 'Learnings'

  def __str__(self):
    return 'learning user : {user}, lesson : {lesson}'.format(user=self.user, lesson=self.lesson)
