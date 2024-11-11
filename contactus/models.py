from django.db import models

# Create your models here.

class SupportMessage(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=150, verbose_name='پست الکترونیکی')
    subject = models.CharField(max_length=100, verbose_name='موضوع پیام')
    message = models.TextField(verbose_name='پیام')
    is_read_by_admin = models.BooleanField(verbose_name='خوانده شده توسط ادمین / نشده')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated_at = models.DateField(auto_now=True, verbose_name='تاریخ اخرین بروز رسانی')
    
    def __str__(self):
        return f'{self.full_name} {self.subject}'
    
    class Meta:
        verbose_name = 'پیام پشتیبانی'
        verbose_name_plural = 'پیام های پشتیبانی'