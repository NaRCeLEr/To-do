# Generated by Django 4.1 on 2023-03-22 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDOList', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(default=2, max_length=150),
            preserve_default=False,
        ),
    ]
