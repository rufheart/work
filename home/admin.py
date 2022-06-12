from django.contrib import admin
from home.models import Product, Order

admin.site.register([Product, Order])

