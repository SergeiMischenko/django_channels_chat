# Generated by Django 5.1.2 on 2024-10-20 06:45

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=12,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+79999999999' or '89999999999'.",
                                regex="^((\\+7)|8)\\d{10}$",
                            )
                        ],
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
