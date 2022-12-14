from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.forms import forms
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from users.forms import NewUserForm, User




def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password1)
            login(request,user)
            return redirect('geolocator:index')
    else:
        form = NewUserForm()
    return render(request, 'registration/register.html', {'form':form})



