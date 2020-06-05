from django.db import models
from django.utils import timezone

class TodoDatabase(models.Model):
        task_id = models.AutoField(primary_key = True)
        task_name = models.CharField(max_length=200)
        timeStamp = models.DateTimeField(default=timezone.now)
        slug = models.CharField(max_length=100)

        def __str__(self):
                return self.task_name + " " +str(self.pk)