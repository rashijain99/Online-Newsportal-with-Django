# Generated by Django 3.2.9 on 2022-01-09 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsblog', '0011_auto_20220109_1824'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='suburb',
            new_name='state',
        ),
    ]
