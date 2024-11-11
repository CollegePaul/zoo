# Generated by Django 5.1.2 on 2024-11-11 10:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_hotelbooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelbooking',
            name='hotel_booking_adults',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hotelbooking',
            name='hotel_booking_children',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hotelbooking',
            name='hotel_booking_oap',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hotelbooking',
            name='hotel_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hotelbooking',
            name='hotel_total_cost',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='hotel_booking_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='hotel_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
