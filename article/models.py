from django.db import models
from authentication.models import User

# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', verbose_name='کاربر')
    image = models.ImageField(upload_to='article', verbose_name='عکس مفاله')
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.TextField(verbose_name='متن مفاله')
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated_at = models.DateField(auto_now=True, verbose_name='تاریخ اخرین بروز رسانی')
    
    def __str__(self):
        return f'{self.title} - {self.user.full_name}'
    
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات' 