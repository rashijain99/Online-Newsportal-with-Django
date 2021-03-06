# Generated by Django 3.2.9 on 2022-01-08 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsblog', '0004_secondleft'),
    ]

    operations = [
        migrations.CreateModel(
            name='thirdfirst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thirdfirst_title', models.CharField(max_length=100)),
                ('thirdfirst_image', models.FileField(default=None, max_length=250, null=True, upload_to='thirdfirst/')),
            ],
        ),
        migrations.CreateModel(
            name='thirdsecond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thirdsecond_title', models.CharField(max_length=100)),
                ('thirdsecond_image', models.FileField(default=None, max_length=250, null=True, upload_to='thirdsecond/')),
            ],
        ),
    ]
