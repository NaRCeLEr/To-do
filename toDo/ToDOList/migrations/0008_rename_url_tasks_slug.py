# Generated by Django 4.1 on 2023-03-24 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDOList', '0007_rename_slug_tasks_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='url',
            new_name='slug',
        ),
    ]
