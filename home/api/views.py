from dataclasses import field
from multiprocessing import context
from rest_framework.views import APIView, Response
from home.models import Order, Product
from home.api.serialize import OrderSerialize



class OrderApi(APIView):
    
    def get(self, request, *args, **kwargs):
        all = Order.objects.all()
        ord = OrderSerialize(all, many=True, context = {'request':request})
        return Response(data=ord.data)
