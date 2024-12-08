from django.urls import path

from . import views

app_name = "api"


urlpatterns = [
    path('products/', views.product_list), 
    path('products/<int:pk>', views.product_detail), 
]