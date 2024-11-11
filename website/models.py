from django.db import models

from django.contrib.auth.models import AbstractUser

class ZooUser(AbstractUser):
    points = models.IntegerField(default=0)
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=14, blank=True)
    icon = models.CharField(max_length=64, default="lion")

class HotelBooking(models.Model):
    
    hotel_user_id = models.ForeignKey(ZooUser, on_delete=models.CASCADE)
    hotel_booking_date = models.DateTimeField(auto_now_add=True)
    hotel_booking_date_arrive = models.DateTimeField()
    hotel_booking_date_leave = models.DateTimeField()
    hotel_booking_adults = models.IntegerField(default=0)
    hotel_booking_children = models.IntegerField(default=0)
    hotel_booking_oap = models.IntegerField(default=0)
    hotel_total_cost = models.FloatField(default=0)
    hotel_points = models.IntegerField(default=0)