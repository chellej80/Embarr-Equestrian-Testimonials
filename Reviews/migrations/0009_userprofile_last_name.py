# Generated by Django 3.2.14 on 2022-07-20 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0008_auto_20220720_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]