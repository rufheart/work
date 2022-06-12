from django import forms
# from django.contrib.auth.models import User
from account.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class FormLogin(AuthenticationForm):   
    pass



class FormRegister(UserCreationForm):
    pass