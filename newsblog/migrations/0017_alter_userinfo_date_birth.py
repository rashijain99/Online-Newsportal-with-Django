# Generated by Django 3.2.9 on 2022-01-09 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsblog', '0016_alter_userinfo_date_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='date_birth',
            field=models.DateField(blank=True, help_text='Please enter DATE in Format - YYYY-MM-DD ', null=True),
        ),
    ]
