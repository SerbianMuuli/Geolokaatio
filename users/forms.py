from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):


	email = forms.EmailField(required=True, label='Sähköposti')

	password1 = forms.CharField(
    label='Salasana',
    strip=False,
    widget=forms.PasswordInput,
    help_text=''
	)

	password2 = forms.CharField(
    label='Salasana uudelleen',
    strip=False,
    widget=forms.PasswordInput,
    help_text=''
	)

	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "email")
		labels = {
            'username': ('Käyttäjänimi'),
			'first_name': ('Etunimi'),
			'last_name': ('Sukunimi'),
        }

		help_texts = {
			'username': ('max. 150 merkkiä: A-Ö, 0-9 , @ . + - _ '),
		}

		error_messages = {
            'username': {
				'max_length': ("Käyttäjänimi enintään 150 merkkiä"),
			} 
        }

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

