# Generated by Django 3.2.14 on 2022-07-24 22:00

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0012_remove_userprofile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=80, verbose_name=django.contrib.auth.models.User),
        ),
    ]