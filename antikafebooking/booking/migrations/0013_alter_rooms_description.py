# Generated by Django 5.0.4 on 2024-05-03 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_alter_rooms_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='description',
            field=models.CharField(blank=True, db_index=True, max_length=255, verbose_name='Описание комнаты'),
        ),
    ]
