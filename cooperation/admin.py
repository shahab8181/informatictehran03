from django.contrib import admin
from .models import RequestingCooperation

# Register your models here.

@admin.register(RequestingCooperation)
class RequestingCooperationAdmin(admin.ModelAdmin):
    pass