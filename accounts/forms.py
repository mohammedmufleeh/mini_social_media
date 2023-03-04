from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User,Image

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'caption']
