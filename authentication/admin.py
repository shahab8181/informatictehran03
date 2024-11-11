from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User

# Register your models here.

admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'auth_token']
    
