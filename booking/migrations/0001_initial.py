# Generated by Django 5.0.1 on 2024-01-20 13:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('train', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_type', models.CharField(blank=True, choices=[('Economy', 'Economy'), ('FirstClass', 'First Class'), ('Business', 'Business'), ('Premium', 'Premium'), ('Luxury', 'Luxury')], max_length=50, null=True)),
                ('seats_booked', models.IntegerField()),
                ('selected_seat', models.CharField(blank=True, max_length=100, null=True)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('from_station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_station', to='train.station')),
                ('to_station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_station', to='train.station')),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='train.train')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
