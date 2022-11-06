from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your model

class Janken(models.Model):
    user_name=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    win_count=models.IntegerField()
    create_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
