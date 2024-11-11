from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    speaker = models.CharField(max_length=100, verbose_name='سخنران')
    description = models.TextField(verbose_name='توضیحات')
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated_at = models.DateField(auto_now=True, verbose_name='تاریخ اخرین بروز رسانی')
    
    def __str__(self):
        return f'{self.title} - {self.speaker}'
    
    class Meta:
        verbose_name = 'رویداد'
        verbose_name_plural = 'رویداد ها'