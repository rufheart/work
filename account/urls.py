from unicodedata import name
from django.urls import path
from account.views import *
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('login', Login_User.as_view(), name='login'),
    path('logout', Logout_User.as_view(), name='logout'),
    path('register/', UserCreate.as_view(), name='register'),
    path('profile/', profile, name='profile')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)