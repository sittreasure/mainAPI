from django.db import models
from base.models import Timestamp

class User(Timestamp):
  name = models.CharField(max_length=30)
  surname = models.CharField(max_length=30)
  avatar = models.TextField()

  class Meta:
    db_table = 'Users'

  def __str__(self):
    return 'user : {name} {surname}'.format(name=self.name, surname=self.surname)
