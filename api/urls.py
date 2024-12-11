from django.urls import path

from . import views

app_name = "api"


urlpatterns = [
    path('products/', views.product_list), 
    path('products/<int:pk>', views.product_detail),
    
    path('orders/', views.order_list), 
    # path('orders/<int:pk>', views.order_detail),
]