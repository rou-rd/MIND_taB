from django.shortcuts import render,redirect
from application.models import conccurent
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import products
from django.shortcuts import render

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserChangeForm

import requests




    




def home(request):
    response = requests.get('http://localhost:5000/prices/')
    datas = response.json()
    return render(request, 'product/product.html',{
        'datas':datas
    
    })