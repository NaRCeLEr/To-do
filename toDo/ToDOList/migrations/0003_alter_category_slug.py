# Generated by Django 4.1 on 2023-03-22 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDOList', '0002_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=150),
        ),
    ]
