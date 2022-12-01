from django.db import models

user_id = 0

def increase_id(id):
    return user_id + 1

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    id = increase_id(user_id)


class Admin_User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    

class Worker_Data(models.Model):
    client_id = models.IntegerField()
    item_name = models.CharField(max_length=50)
    url = models.CharField(max_length=1000)
    demand_price = models.IntegerField()