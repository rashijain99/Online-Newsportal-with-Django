# Generated by Django 3.2.9 on 2022-01-07 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='news/'),
        ),
    ]