from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from .models import User, Otp
import random


# @receiver(signal=post_save, sender=User)
# def make_otp_code_for_user(sender: User, instance, *args, **kwargs):
#     Otp.objects.create(user=instance, phone_number=instance.phone_number, code=random.randint(1000, 9999))


@receiver(signal=post_save, sender=Otp)
def make_token_for_user(sender: User, instance, *args, **kwargs):
    TOKEN, created = Token.objects.get_or_create(user_id=instance.user.id)
    if created:
        instance.delete()
        TOKEN.user.is_active = True
        TOKEN.user.save()