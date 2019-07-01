# Generated by Django 2.1 on 2019-07-01 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20190701_1201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schooluser',
            old_name='name',
            new_name='firstname',
        ),
        migrations.RemoveField(
            model_name='schooluser',
            name='f_name',
        ),
        migrations.RemoveField(
            model_name='schooluser',
            name='m_nane',
        ),
        migrations.AddField(
            model_name='schooluser',
            name='lastname',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
