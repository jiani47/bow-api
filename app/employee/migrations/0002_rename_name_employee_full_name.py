# Generated by Django 3.2.15 on 2022-09-19 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='name',
            new_name='full_name',
        ),
    ]
