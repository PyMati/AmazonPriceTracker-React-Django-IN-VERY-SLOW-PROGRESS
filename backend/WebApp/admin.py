from django.contrib import admin
from .models import User, Admin_User, Worker_Data
# Register your models here.
admin.site.register(User)
admin.site.register(Admin_User)
admin.site.register(Worker_Data)