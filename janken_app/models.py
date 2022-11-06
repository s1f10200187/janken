from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your model

class Janken(models.Model):
    user_name=models.CharField(max_length=20)
    win=models.IntegerField()

    def __str__(self):
        return self.user_name

    def publish(self):
        self.published_date = timezone.now()
        self.save()
