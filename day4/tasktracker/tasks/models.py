from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50, default="pending")
    created_date = models.DateTimeField(auto_now_add=True)