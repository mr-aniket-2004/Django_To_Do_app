from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField()
    description = models.CharField(default=None)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

