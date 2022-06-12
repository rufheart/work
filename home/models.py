from ast import Delete
from email.mime import image
from itertools import product
from unicodedata import name
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class ABS(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class meta():
        abstract = True

class Product(ABS):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to = 'img/product')

class Order(ABS):
    client=models.ForeignKey(User, related_name='order', on_delete=models.CASCADE)
    order_product=models.ForeignKey(Product, related_name='order', on_delete=models.CASCADE)    
    country = models.CharField(max_length=60)
    price = models.CharField(max_length=50)
    order_count = models.DecimalField(max_digits=20, decimal_places=0)
