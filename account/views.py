from distutils import errors
from re import template
from webbrowser import get
from django import dispatch
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
# from django.contrib.auth.models import User
# from account.models import User
from account.forms import FormLogin, FormRegister
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model
import json

User = get_user_model()



class Login_User(LoginView):
    template_name = 'login.html'
    succes_url = reverse_lazy('profile')
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('profile'))
        return super().dispatch(request, *args, **kwargs)

class Logout_User(LogoutView):
    pass



class UserCreate(CreateView):
    template_name = 'register.html'
    form_class = FormRegister
    success_url = reverse_lazy('login')

def profile(request):
    args = {}
    user = User
    print('prof')
    if request.method == 'POST':
        print('if isledi')
        form = FormUpdate_Profile(data=request.POST, files=request.FILES)
        if form.is_valid():
            print('validisledi')
            form.save(request.user.id)
        else:
            print('=============>', form.errors)

    else:
        form = FormUpdate_Profile()
    
    form.initial['username'] = request.user.username
    form.initial['first_name'] = request.user.first_name
    form.initial['last_name'] = request.user.last_name
    form.initial['email'] = request.user.email
    form.initial['password'] = request.user.password

    user = User.objects.get(id = request.user.id)
    user = dict(username = user.username, password = user.password)

    args = {
        'form':form,
        'user1':User.objects.get(id=request.user.id),
        'user': json.dumps(user)
        }

    return render(request, 'profile.html', args)    