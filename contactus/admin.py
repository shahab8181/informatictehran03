from django.contrib import admin
from .models import SupportMessage

# Register your models here.

@admin.register(SupportMessage)
class SupportMessageAdmin(admin.ModelAdmin):
    pass