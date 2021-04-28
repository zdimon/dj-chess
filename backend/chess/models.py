from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(User):
    publicname = models.CharField(default='', max_length=250)


class SocialAuth(models.Model):
    type = models.CharField(max_length=50)
    email =  models.CharField(max_length=50)
    secret =  models.CharField(max_length=250)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE) 