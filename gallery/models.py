from django.db import models

# Create your models here.

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery', verbose_name='تصویر')
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated_at = models.DateField(auto_now=True, verbose_name='تاریخ اخرین بروز رسانی')
    
    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'