# Generated by Django 3.2.15 on 2022-11-03 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibition',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='exhibition',
            name='start_date',
            field=models.DateField(),
        ),
    ]