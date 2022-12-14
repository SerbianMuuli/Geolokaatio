from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm, EditProfileForm
from .models import ImagesDB
import folium
from folium.plugins import LocateControl
import gagl.settings
from users.forms import User
from django.contrib import messages
from django.forms import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.
def index(request):
    return render(request, 'geolocator/index.html')

def add_image(request):

    if request.method != 'POST':
        form = NewImageForm()
    else:
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = form.save(commit=False)
            new_image.sender = request.user
            new_image.location = new_image.image_lat_long[7:].replace(")","")
            new_image.save()
            return redirect('geolocator:list_images')
    context = {'form': form}

    return render(request, 'geolocator/add_image.html', context)

def main_page(request):
    return render(request, 'geolocator/main_page.html')

def list_images(request):
    # fetch all image_items from database
    all_images = ImagesDB.objects.all()
    # create a map object with folium
    image_map = folium.Map(zoom_start=15)

    LocateControl(auto_start=True, flyTo =True).add_to(image_map)

    # create markers to folium map
    for coordinate in all_images:
        coords = coordinate.location.split(",")
        latitude = coords[0]
        longitude = coords[1]
        description = coordinate.description
        image = coordinate.image.url

        image_frame =   f"""
                        <p>
                            <img src='{image}' alt='Img' width='100'>

                        </p>"""




        folium.Marker(
            location=[latitude, longitude],
            popup=image_frame,
            icon=folium.Icon(color="red")
        ).add_to(image_map)

    
    
    image_map=image_map._repr_html_()
    context = {'image_map': image_map}
    
    return render(request, 'geolocator/list_images.html', context)



#users profile and personal pictures
def profile(request):
    imgcount = len(ImagesDB.objects.all())
    context = {'imageCount': imgcount}
    return render(request, 'geolocator/profile.html', context)

#ability to change profile information
def edit_profile(request):
    if request.method == 'POST':
        #Inherit EditProfileForm from form so that user's can only change selected parts
        form = EditProfileForm(request.POST, instance=request.user)
        
        #if form is valid. Then save it and return user back to profile page
        if form.is_valid():
            form.save()
            return render(request, 'geolocator/profile.html')
    else:
        form = EditProfileForm(instance=request.user)
        context = {'form': form}
        return render(request, 'geolocator/edit_profile.html', context)


def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user=request.user)
        #if form is valid. Then save it and return user back to profile page
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, '/geolocator/profile.html')
        else:
            return redirect('/profile/password/')
    else:
        form = PasswordChangeForm(user=request.user)
        context = {'form': form}
        return render(request, 'geolocator/password.html', context)

