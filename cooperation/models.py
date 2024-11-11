from django.db import models
from job_opportunity.models import JobOpportunity

# Create your models here.

class RequestingCooperation(models.Model):
    job_opportunity = models.ForeignKey(JobOpportunity, on_delete=models.CASCADE, blank=True, null=True, related_name='requests', verbose_name='فرصت شغلی')
    full_name = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=254, verbose_name='پست الکترونیکی')
    phone_number = models.CharField(max_length=11, verbose_name='شماره تماس')
    gender = models.CharField(max_length=5, verbose_name='جنسیت')
    date_of_birth = models.CharField(max_length=200, verbose_name='تاریخ تولد')
    marital_status = models.CharField(max_length=100, verbose_name='وضعیت تاهل')
    military_status = models.CharField(max_length=150, verbose_name='وضعیت نظام وظیفه')
    type_of_cooperation = models.CharField(max_length=150, verbose_name='نوع همکاری')
    rights_requested = models.PositiveBigIntegerField(verbose_name='حقوق درخواستی')
    description = models.TextField(verbose_name='توضیحات درباره همکاری')
    resume = models.FileField(upload_to='resumes', verbose_name='فایل رزومه')
    avatar = models.ImageField(upload_to='collaboration_avatars', verbose_name='تصویر پروفایل')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated_at = models.DateField(auto_now=True, verbose_name='تاریخ اخرین بروز رسانی')
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'درخواست همکاری'
        verbose_name_plural = 'درخواست های همکاری'