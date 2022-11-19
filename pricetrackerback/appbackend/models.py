from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    running_workers =models.IntegerField(default=0)
    