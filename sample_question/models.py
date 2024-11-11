from django.db import models

# Create your models here.

class FieldOfStudy(models.Model):
    name = models.CharField(max_length=150, verbose_name='نام رشته')
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated_at = models.DateField(auto_now=True, verbose_name='تاریخ اخرین بروز رسانی')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'رشته'
        verbose_name_plural = 'رشته ها'
        


class Lesson(models.Model):
    field_of_study = models.ForeignKey(FieldOfStudy, on_delete=models.CASCADE, blank=True, null=True, related_name='lessons', verbose_name='رشته')
    name = models.CharField(max_length=150, verbose_name='نام رشته')
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated_at = models.DateField(auto_now=True, verbose_name='تاریخ اخرین بروز رسانی')
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'درس'
        verbose_name_plural = 'درس ها'