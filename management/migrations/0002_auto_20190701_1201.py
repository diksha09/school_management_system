# Generated by Django 2.1 on 2019-07-01 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schooluser',
            old_name='s_name',
            new_name='name',
        ),
    ]
