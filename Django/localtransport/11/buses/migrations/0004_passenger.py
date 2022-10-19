# Generated by Django 4.1.2 on 2022-10-10 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0003_rename_buses_bus_rename_stations_station'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('buses', models.ManyToManyField(blank=True, related_name='passengers', to='buses.bus')),
            ],
        ),
    ]
