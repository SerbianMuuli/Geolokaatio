from django import forms
from .models import ImagesDB
from location_field.forms.plain import PlainLocationField
from users.forms import User
from django.contrib.auth.forms import UserChangeForm

class NewImageForm(forms.ModelForm):
    class Meta:
        model = ImagesDB
        fields = ['image','description','image_lat_long']

        labels = {
            'image': ('Lataa kuva '),
            'description': ('Kuvaus '),
            'image_lat_long': ('Pituus- ja leveysasteet'),
        }
        
        widgets = {
            'image_lat_long': forms.Textarea(attrs={'rows':5,
                                            'cols':35,
                                            'style':'resize:none;'}),
            'description': forms.Textarea(attrs={'rows':5,
                                            'cols':35,
                                            'style':'resize:none;'}),
        }



class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        #This specifies which parts user can change
        fields = ['username','first_name','last_name','password']

        labels = {
            'username': ('Käyttäjänimi'),
			'first_name': ('Etunimi'),
			'last_name': ('Sukunimi'),
            'password': ('salasana')
        }
        
        help_texts = {
			'username': ('max. 150 merkkiä: A-Ö, 0-9 , @ . + - _ '),
		}
        
        error_messages = {
            'username': {
				'max_length': ("Käyttäjänimi enintään 150 merkkiä"),
			} 
        }