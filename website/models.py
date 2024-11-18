from django.db import models

from django.contrib.auth.models import AbstractUser

class ZooUser(AbstractUser):
    points = models.IntegerField(default=0)
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=14, blank=True)
    icon = models.CharField(max_length=64, default="lion")

class HotelBooking(models.Model):
    
    booking_id = models.AutoField(primary_key=True, editable=False)
    hotel_user_id = models.ForeignKey(ZooUser, on_delete=models.CASCADE)
    hotel_booking_date = models.DateField(auto_now_add=True)
    hotel_booking_date_arrive = models.DateField()
    hotel_booking_date_leave = models.DateField()
    hotel_booking_adults = models.IntegerField(default=0)
    hotel_booking_children = models.IntegerField(default=0)
    hotel_booking_oap = models.IntegerField(default=0)
    hotel_total_cost = models.FloatField(default=0)
    hotel_points = models.IntegerField(default=0)


class ZooBooking(models.Model):
    
    booking_id = models.AutoField(primary_key=True, editable=False)
    zoo_user_id = models.ForeignKey(ZooUser, on_delete=models.CASCADE)
    zoo_booking_date = models.DateField(auto_now_add=True)
    zoo_booking_date_arrive = models.DateField()
    zoo_booking_date_leave = models.DateField()
    zoo_booking_adults = models.IntegerField(default=0)
    zoo_booking_children = models.IntegerField(default=0)
    zoo_booking_oap = models.IntegerField(default=0)
    zoo_total_cost = models.FloatField(default=0)
    zoo_points = models.IntegerField(default=0)

