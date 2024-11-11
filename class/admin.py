from django.contrib import admin
from .models import Class

# Register your models here.

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'number_of_class', 'teacher']