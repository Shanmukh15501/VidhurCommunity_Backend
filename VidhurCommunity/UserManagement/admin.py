from django.contrib import admin
from UserManagement.models import Users
from django.contrib.auth.models import Group, User

class UsersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Users._meta.fields]
   

admin.site.register(Users, UsersAdmin)