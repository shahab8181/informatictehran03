# Generated by Django 5.1.2 on 2024-11-10 09:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FieldOfStudy",
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
                ("name", models.CharField(max_length=150, verbose_name="نام رشته")),
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
                "verbose_name": "رشته",
                "verbose_name_plural": "رشته ها",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
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
                ("name", models.CharField(max_length=150, verbose_name="نام رشته")),
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
                (
                    "field_of_study",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lessons",
                        to="sample_question.fieldofstudy",
                        verbose_name="رشته",
                    ),
                ),
            ],
            options={
                "verbose_name": "درس",
                "verbose_name_plural": "درس ها",
            },
        ),
    ]