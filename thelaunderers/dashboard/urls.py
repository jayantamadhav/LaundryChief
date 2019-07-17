from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('orderStatus', views.orderStatus, name='orderStatus'),
    path('customers', views.customers, name='customers'),
    path('salesMetrics', views.salesMetrics, name="salesMetrics"),
    path('customers/getOrderHistory', views.getOrderHistory, name="getOrderHistory"),
    path('cartdata', views.getData, name='cartdata'),	
    path('generateInvoice/<int:id>', views.generateInvoice, name="generateInvoice"),
]
