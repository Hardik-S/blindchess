from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Game(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    challenger = models.CharField(max_length=100)
    mode = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.mode
