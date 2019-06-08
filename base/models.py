from django.db import models

class Timestamp(models.Model):
  id = models.AutoField(primary_key=True)
  createdAt = models.DateTimeField(db_column='created_at', auto_now_add=True)
  updatedAt = models.DateTimeField(db_column='updated_at', auto_now=True)

  class Meta:
    abstract = True
