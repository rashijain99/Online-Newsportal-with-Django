# Generated by Django 3.2.9 on 2022-01-07 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsblog', '0002_news_news_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='firstsidenews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstsidenews_title', models.CharField(max_length=100)),
                ('firstsidenews_image', models.FileField(default=None, max_length=250, null=True, upload_to='firstsidenews/')),
            ],
        ),
    ]
