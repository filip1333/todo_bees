from django.db import models
from django.utils import timezone


class ToDoList(models.Model):
    completed = models.BooleanField(default=False)
    task = models.CharField(max_length=250)
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
