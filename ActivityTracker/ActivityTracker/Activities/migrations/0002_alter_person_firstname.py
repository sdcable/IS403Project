# Generated by Django 4.1.2 on 2022-11-14 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='firstname',
            field=models.CharField(max_length=40),
        ),
    ]
