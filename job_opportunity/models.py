from django.db import models

# Create your models here.

class JobOpportunity(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True, verbose_name='عنوان')
    place = models.CharField(max_length=300, blank=True, null=True, verbose_name='مکان')
    description = models.TextField(verbose_name='شرح موقعیت شغلی')
    gender = models.CharField(max_length=5, verbose_name='جنسیت')
    age = models.CharField(max_length=250, verbose_name='سن')
    literacy_level = models.CharField(max_length=200, verbose_name='سطح سواد')
    minimum_work_experience = models.CharField(max_length=200, verbose_name='حداقل سابقه کاری مورد نیاز')
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated_at = models.DateField(auto_now=True, verbose_name='تاریخ اخرین بروز رسانی')
    
    class Meta:
        verbose_name = 'فرصت شغلی'
        verbose_name_plural = 'فرصت های شغلی'