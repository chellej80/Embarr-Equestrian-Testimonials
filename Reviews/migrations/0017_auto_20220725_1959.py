# Generated by Django 3.2.14 on 2022-07-25 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0016_remove_comment_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('location', models.CharField(default='e.g Dublin', max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')], default='5 stars')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='Reviews.post')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]