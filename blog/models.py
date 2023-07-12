from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BlogPost(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    headline = models.CharField(max_length=170)
    desc = models.TextField()