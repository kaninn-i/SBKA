# Generated by Django 5.0.4 on 2024-04-16 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_rooms_floor_alter_booking_how_many_visitors_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms',
            name='floor',
        ),
    ]
