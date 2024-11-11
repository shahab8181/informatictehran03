# Generated by Django 5.1.2 on 2024-10-28 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Class",
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
                    "number_of_class",
                    models.PositiveSmallIntegerField(verbose_name="شماره کلاس"),
                ),
                (
                    "day",
                    models.CharField(
                        choices=[
                            ("SATURDAY", "شنبه"),
                            ("SUNDAY", "یک شنبه"),
                            ("MONDAY", "دوشنبه"),
                            ("TUESDAY", "سه شنبه"),
                            ("WEDNESDAY", "چهار شنبه"),
                            ("THURSDAY", "پنج شنبه"),
                            ("FRIDAY", "جمعه"),
                        ],
                        max_length=100,
                        verbose_name="روز کلاس",
                    ),
                ),
                ("lesson", models.CharField(max_length=200, verbose_name="درس")),
                ("teacher", models.CharField(max_length=200, verbose_name="استاد")),
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
                "verbose_name": "کلاس",
                "verbose_name_plural": "کلاس ها",
            },
        ),
    ]