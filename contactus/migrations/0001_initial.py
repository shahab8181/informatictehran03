# Generated by Django 5.1.2 on 2024-11-06 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SupportMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "full_name",
                    models.CharField(max_length=200, verbose_name="نام و نام خانوادگی"),
                ),
                (
                    "email",
                    models.EmailField(max_length=150, verbose_name="پست الکترونیکی"),
                ),
                (
                    "subject",
                    models.CharField(max_length=100, verbose_name="موضوع پیام"),
                ),
                ("message", models.TextField(verbose_name="پیام")),
                (
                    "is_read_by_admin",
                    models.BooleanField(verbose_name="خوانده شده توسط ادمین / نشده"),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد"),
                ),
                (
                    "updated_at",
                    models.DateField(
                        auto_now=True, verbose_name="تاریخ اخرین بروز رسانی"
                    ),
                ),
            ],
            options={
                "verbose_name": "پیام پشتیبانی",
                "verbose_name_plural": "پیام های پشتیبانی",
            },
        ),
    ]
