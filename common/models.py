from django.db import models
from django.utils import timezone

COMPLETE_CHOICES = [
    ('True', 'Completed'),
    ('False', 'Uncompleted'),
]


class ToDoList(models.Model):
    COMPLETED = 'True'
    UNCOMPLETED = 'False'
    COMPLETE_CHOICES = [
        (COMPLETED, 'Completed'), (UNCOMPLETED, 'Uncompleted')
    ]
    completed = models.CharField(max_length=2, choices=COMPLETE_CHOICES, default=UNCOMPLETED,)
    task = models.CharField(max_length=250)
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
