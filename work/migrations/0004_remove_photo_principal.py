# Generated by Django 3.2.15 on 2022-10-05 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0003_painting_caption'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='principal',
        ),
    ]
