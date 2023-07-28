from django.shortcuts import render 
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.

@login_required
def dashboard(request): #main screen
    return render(request, 'registration/dashboard.html',{'section':'dashboard'})

