from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

'''
class PlayerRegisterForm(UserRegisterForm):
    nickName = forms.CharField()

class DevRegisterForm(UserRegisterForm):
    iban = forms.CharField()
'''
# Make different forms if different data needed for player/dev