from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from usuarios.models import UserProfile

class RegisterForm(UserCreationForm):
    first_name  = forms.CharField(max_length=50, required=True, label='Nombre')
    last_name  = forms.CharField(max_length=50, required=True, label='Apellido')

    class Meta:
        model = User
        #fields = ['username','first_name','last_name','email','password','password2']
        fields = ['username','first_name','last_name','email']

class UpdateForm(forms.ModelForm):
    #username = forms.CharField(max_length=50, required=True, label='Usuario')
    first_name  = forms.CharField(max_length=50, required=True, label='Nombre')
    last_name  = forms.CharField(max_length=50, required=True, label='Apellido')

    class Meta:
        model = User
        fields = ['first_name','last_name']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['telefono','fecha_nacimiento','foto']
