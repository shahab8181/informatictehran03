# Generated by Django 5.1.2 on 2024-11-07 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Gallery",
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
                ("image", models.ImageField(upload_to="gallery", verbose_name="تصویر")),
                ("is_active", models.BooleanField(verbose_name="فعال / غیر فعال")),
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
                "verbose_name": "تصویر",
                "verbose_name_plural": "تصاویر",
            },
        ),
    ]