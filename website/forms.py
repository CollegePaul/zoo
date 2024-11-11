from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput

from .models import ZooUser,HotelBooking


# - Register or Create a user
class CreateUserForm(UserCreationForm):

    class Meta:
        model = ZooUser
        fields = ['username', 'password1', 'password2']


# - Login User
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# - hotel booking
class Hotel_Booking_Form(HotelBooking):
    
    
    hotel_booking_date_arrive =  forms.DateTimeField(widget=forms.DateInput(format="%d/%m/%Y"))
    hotel_booking_date_leave = forms.DateTimeField(widget=forms.DateInput(format="%d/%m/%Y"), label='Date Leave')
    hotel_booking_adults = forms.DateTimeField(widget=TextInput())
    hotel_booking_children = forms.IntegerField(widget=TextInput())
    hotel_booking_oap = forms.IntegerField(widget=TextInput())
    hotel_total_cost = forms.IntegerField(widget=TextInput())
    # hotel_points = models.IntegerField(default=0)
    fields = ['hotel_booking_date_arrive', 'hotel_booking_date_leave']

   