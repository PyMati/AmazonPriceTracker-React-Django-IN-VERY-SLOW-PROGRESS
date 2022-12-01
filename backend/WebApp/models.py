from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)


class Admin_User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    

class Worker_Data(models.Model):
    client_id = models.IntegerField()
    item_name = models.CharField(max_length=50)
    url = models.CharField(max_length=1000)
    demand_price = models.IntegerField()