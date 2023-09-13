# Generated by Django 4.2.4 on 2023-09-07 20:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='porfolio/images')),
                ('url', models.URLField(blank=True)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
