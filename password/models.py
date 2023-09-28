from django.db import models
from account.models import UserProfile

class Password(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_password')
    website = models.CharField(max_length=255)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.website} - {self.username}"