# Generated by Django 4.2.6 on 2023-10-19 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0002_alter_details_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='address_line',
        ),
        migrations.AlterField(
            model_name='details',
            name='postcode',
            field=models.IntegerField(),
        ),
    ]
