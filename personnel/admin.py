from django.contrib import admin
from .models import Personnel

# Register your models here.

@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'personnel_type', 'job']