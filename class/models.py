from django.db import models

# Create your models here.
    
class Class(models.Model):
    class DaysChoices(models.TextChoices):
        SATURDAY = 'SATURDAY', 'شنبه'
        SUNDAY = 'SUNDAY', 'یک شنبه'
        MONDAY = 'MONDAY', 'دوشنبه'
        TUESDAY = 'TUESDAY', 'سه شنبه'
        WEDNESDAY = 'WEDNESDAY', 'چهار شنبه'
        THURSDAY = 'THURSDAY', 'پنج شنبه'
        FRIDAY = 'FRIDAY', 'جمعه'
        
    number_of_class = models.PositiveSmallIntegerField(verbose_name='شماره کلاس')
    day = models.CharField(max_length=100, choices=DaysChoices.choices, verbose_name='روز کلاس')
    lesson = models.CharField(max_length=200, verbose_name='درس')
    teacher = models.CharField(max_length=200, verbose_name='استاد')
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated_at = models.DateField(auto_now=True, verbose_name='تاریخ اخرین بروز رسانی')
    
    def __str__(self):
        return self.lesson
    
    class Meta:
        verbose_name = 'کلاس'
        verbose_name_plural = 'کلاس ها'