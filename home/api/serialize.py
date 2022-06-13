from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from home.models import Order, Product
from account.models import User


class UserSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class ProductSerialize(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name')


class OrderSerialize(serializers.ModelSerializer):
    client = UserSerialize()
    order_product = ProductSerialize()
    class Meta:
        model = Order
        fields = ('client','order_product','country','price','order_count')