from django.urls import path

from . import views

app_name = "api"


urlpatterns = [
    path('products/', views.product_list),
    path('products/info/', views.product_info),
    path('products/<int:pk>/', views.product_detail),
    
    path('orders/', views.order_list), 
    path('user-orders/', views.user_order_list, name="user-orders"), 
    # path('orders/<int:pk>', views.order_detail),
]