from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import UserManager

# Create your models here.

class User(AbstractUser):
    username = models.NOT_PROVIDED()
    
    full_name = models.CharField(max_length=200, blank=False, null=False, verbose_name='نام و نام خانوادگی')
    phone_number = models.CharField(max_length=11, unique=True, blank=False, null=False, verbose_name='شماره همراه')
    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated_at = models.DateField(auto_now=True, verbose_name='تاریخ اخرین بروز رسانی')
    
    USERNAME_FIELD = 'phone_number'
    
    objects = UserManager()
    
    def __str__(self):
        return f'{self.full_name} - {self.phone_number}'
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران' 
    


class Otp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, db_index=True, related_name='otp', verbose_name='کاربر')
    phone_number = models.CharField(max_length=11, blank=True, null=True, db_index=True, verbose_name='شماره تلفن')
    code = models.CharField(max_length=6, blank=True, null=True, verbose_name='کد')
    attempts = models.PositiveSmallIntegerField(default=0, blank=True, null=True, verbose_name='تعداد تلاش')
    created = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='تاریخ انقضا')
    
    def __str__(self):
        return f'{self.user.full_name} {self.user.phone_number}'
    
    class Meta:
        default_manager_name = 'objects'
        verbose_name = 'رمز یکبار مصرف'
        verbose_name_plural = 'لیست رمز یکبار مصرف'

    