from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.TextField(verbose_name='سوال')
    answer = models.TextField(verbose_name='پاسخ')
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated_at = models.DateField(auto_now=True, verbose_name='تاریخ اخرین بروز رسانی')
    
    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = 'پرسش و پاسخ'
        verbose_name_plural = 'پرسش ها و پاسخ ها'