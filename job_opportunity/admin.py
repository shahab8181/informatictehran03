from django.contrib import admin
from .models import JobOpportunity

# Register your models here.

@admin.register(JobOpportunity)
class JobOpportunityAdmin(admin.ModelAdmin):
    pass