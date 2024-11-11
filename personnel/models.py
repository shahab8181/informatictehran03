from django.db import models

# Create your models here.

class Personnel(models.Model):
    class PersonnelTypeChoices(models.TextChoices):
        TEACHER = 'TEACHER', 'استاد'
        STAFF = 'STAFF', 'کارمند'
        
    image = models.ImageField(upload_to='personnel_images', verbose_name='عکس پرسنل')
    full_name = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')
    personnel_type = models.CharField(max_length=100, choices=PersonnelTypeChoices.choices, verbose_name='نوع پرسنل')
    job = models.CharField(max_length=200, verbose_name='شغل')
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated_at = models.DateField(auto_now=True, verbose_name='تاریخ اخرین بروز رسانی')
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'پرسنل'
        verbose_name_plural = 'لیست پرسنل'
        