# Generated by Django 3.2 on 2021-05-01 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_user_managers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='User_data',
        ),
    ]
