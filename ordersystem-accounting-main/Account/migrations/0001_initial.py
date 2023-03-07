# Generated by Django 4.1.7 on 2023-03-07 14:54

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
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
                ("FirstName", models.CharField(max_length=20)),
                ("LastName", models.CharField(max_length=20)),
                ("CheckedIn", models.BooleanField(default=False)),
                ("Balance", models.IntegerField()),
            ],
        ),
    ]
