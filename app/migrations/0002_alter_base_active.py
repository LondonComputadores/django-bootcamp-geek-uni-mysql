# Generated by Django 3.2.7 on 2021-09-19 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]
