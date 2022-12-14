
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'geolocator'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_image/', views.add_image, name='add_image'),
    path('main_page/', views.main_page, name='main_page'),
    path('list_images/', views.list_images, name="list_images"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logged_out.html'),name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/password/', views.password, name='password'),
    
]