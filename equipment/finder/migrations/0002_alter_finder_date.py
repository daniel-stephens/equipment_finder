# Generated by Django 3.2.9 on 2021-11-19 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finder',
            name='date',
            field=models.DateField(default='21/08/2021'),
        ),
    ]
