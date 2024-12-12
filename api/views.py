from django.db.models import Max
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import Order, Product
from .serializers import OrderSerializer, ProductInfoSerializer, ProductSerializer



class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    

class OrderList(generics.ListAPIView):
    queryset = Order.objects.prefetch_related("items", "items__product")
    serializer_class = OrderSerializer


@api_view(["GET"])
def product_info(request):
    products = Product.objects.all()
    data = {
        "products": products,
        "count": products.count,
        "max_price": products.aggregate(max_price=Max("price"))["max_price"],
    }
    serializer = ProductInfoSerializer(data)
    return Response(serializer.data)


product_list = ProductList.as_view()
product_detail = ProductDetail.as_view()
order_list = OrderList.as_view()