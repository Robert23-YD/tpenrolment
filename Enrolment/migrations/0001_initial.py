# Generated by Django 5.0.2 on 2024-12-11 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("s_name", models.CharField(max_length=200)),
                ("s_fathername", models.CharField(max_length=200)),
                ("s_mothername", models.CharField(max_length=200)),
                ("s_addr", models.CharField(max_length=200)),
                ("s_school", models.CharField(max_length=200)),
                ("s_email", models.EmailField(max_length=200)),
                ("s_gender", models.CharField(max_length=200)),
                ("s_class", models.CharField(max_length=200)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
            ],
        ),
    ]
