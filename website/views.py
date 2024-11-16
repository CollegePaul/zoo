from django.shortcuts import render,  redirect
from .forms import CreateUserForm, LoginForm,Hotel_Booking_Form

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    return render(request, 'website/index.html')

# register a user
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form  = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            #messages.success(request, "Account created successfully!")
            return redirect('my-login')
    
    context = {'form':form}

    return render(request,'website/register.html', context=context)


# login a user

def my_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('')

    context = {'login_form':form}
    return render(request,'website/my-login.html', context=context)

def user_logout(request):
    auth.logout(request)
    return redirect("website/my-login")

@login_required(login_url='my-login')
def hotel(request):
    
    form = Hotel_Booking_Form()
    

    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False) # Return an object without saving to the DB
            obj.hotel_user_id = request.user # Add the hotel_user_id field with the user object
            obj.save() # Save to database
            
            messages.success(request, "Hotel booked successfully!")
            return redirect('')
    
    context = {'form': form}

    return render(request, 'website/hotel.html', context=context)


def education(request):
    return render(request, 'website/education.html')

def test(request):
    return render(request,'website/test.html')
