from django.urls import path
from . import views

urlpatterns = [
     path('', views.dashboard , name='dashboard'),
     path('viewOrders', views.viewOrders , name='viewOrders'),
     path('addOrder', views.addOrder , name='addOrder'),
     path('editOrder/<int:pk>', views.editOrder , name='editOrder'),
     path('deleteOrder/<int:pk>', views.deleteOrder , name='deleteOrder'),
     path('productDetail/<int:pk>', views.productDetail , name='productDetail'),
     
]
