# Generated by Django 3.2.9 on 2021-11-12 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Finder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='Not described', max_length=200)),
                ('rating', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finder.equipment')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finder.location')),
            ],
        ),
    ]
