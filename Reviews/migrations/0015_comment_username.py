# Generated by Django 3.2.14 on 2022-07-24 22:23

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0014_alter_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(default='Input your username', max_length=20, verbose_name=django.contrib.auth.models.User),
        ),
    ]
