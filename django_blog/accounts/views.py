
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))  
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    
    return render(request, 'profile.html', {'user': user})




def login_view(request):
    return HttpResponse("Login Page")

def logout_view(request):
    return HttpResponse("Logout Page")

def register_view(request):
    return HttpResponse("Registration Page")

def profile_view(request):
    return HttpResponse("User Profile Page")




def profile_management_view(request):
    if request.method == 'POST':
        # Handle form submission to update user information
        # Logic to update user details
        return HttpResponse("Profile updated successfully!")
    else:
        # Retrieve and display user profile information
        # Logic to fetch and display user details
        return HttpResponse("User Profile Page")
