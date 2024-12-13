from django.db.models import Max
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Order, Product
from .serializers import OrderSerializer, ProductInfoSerializer, ProductSerializer



class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    

class OrderList(generics.ListAPIView):
    queryset = Order.objects.prefetch_related("items", "items__product")
    serializer_class = OrderSerializer


class UserOrderList(generics.ListAPIView):
    queryset = Order.objects.prefetch_related("items", "items__product")
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)




class ProductInfo(APIView):
    def get(self, request):
        products = Product.objects.all()
        data = {
            "products": products,
            "count": products.count,
            "max_price": products.aggregate(max_price=Max("price"))["max_price"],
        }
        serializer = ProductInfoSerializer(data)
        return Response(serializer.data)


product_list = ProductListCreate.as_view()
product_detail = ProductDetail.as_view()
product_info = ProductInfo.as_view()
order_list = OrderList.as_view()
user_order_list = UserOrderList.as_view()
