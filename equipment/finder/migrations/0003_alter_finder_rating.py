# Generated by Django 3.2.9 on 2021-11-19 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0002_alter_finder_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finder',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]
