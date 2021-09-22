from django.urls import path
from django.urls.conf import include
import rest_framework

from rest_framework.routers import DefaultRouter

from api.views import ProductDetailView, ProductListView, Register


urlpatterns = [

    path('product/',ProductListView.as_view(),name='Product-List'),
    path('product/<int:pk>',ProductDetailView.as_view(),name='Product-Detail'),
    path('register/',Register.as_view(),name='Register'),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
    
]