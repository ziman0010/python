from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    description = models.TextField()
