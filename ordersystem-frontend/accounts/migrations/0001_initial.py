# Generated by Django 2.2.7 on 2019-11-16 14:29

from django.db import migrations, models

from django.db import migrations
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('used', models.BooleanField(default=False)),
            ],
        ),
    ]