#from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
       class Meta:
         model = User
         fields = ['username','first_name','last_name','email','password1','password2']
        #fields = ['email','rut','name','last_name','password']
        #se le agregaron mas parametros para el formulario de registro, pero ojo, estos datos
        #YA EXISTEN en la tabla user, solo se evocaron


