# Generated by Django 3.2.9 on 2022-01-08 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsblog', '0007_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(choices=[('MR', 'Mr.'), ('MRS', 'Mrs.'), ('MS', 'Ms.')], max_length=3)),
                ('mobile', models.CharField(max_length=15)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]