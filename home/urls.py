from django.urls import path
from home.views import firstview

urlpatterns = [
    path('', firstview, name='firstview'),
]