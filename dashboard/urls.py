from django.urls import path
from . import views

urlpatterns = [
     path('', views.dashboard , name='dashboard'),
     path('order', views.order , name='order'),
     path('editorder/<int:pk>', views.editorder , name='editorder'),
     path('deleteorder/<int:pk>', views.deleteorder , name='deleteorder'),
     
]
