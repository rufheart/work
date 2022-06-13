from django.urls import URLPattern, path
from home.api.views import OrderApi

urlpatterns = [
    path('order/', OrderApi.as_view())
]