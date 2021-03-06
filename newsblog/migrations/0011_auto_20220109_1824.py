# Generated by Django 3.2.9 on 2022-01-09 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsblog', '0010_auto_20220109_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='email_confirmed',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='addressLine1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='addressLine2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='marital_status',
            field=models.CharField(choices=[('MARRIED', 'Married'), ('SINGLE', 'Single'), ('WIDOWED', 'Widowed'), ('DIVORCED', 'Divorced')], default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='sex',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='suburb',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
