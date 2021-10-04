from django.urls import path
from django.urls.conf import include




from api.views import ProductDetailView, ProductListView, catagory,ProductListAdminView,ProductDetailAdminView




urlpatterns = [

    path('product/',ProductListView.as_view(),name='Product-List'),
    path('product/<int:P_id>',ProductDetailView.as_view(),name='Product-Detail'),
    # path('register/',Register.as_view(),name='Register'),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('admin/',ProductListAdminView.as_view(),name='All_Product'),
    path('admin/<int:pk>',ProductDetailAdminView.as_view(),name='Product CRUD'),
    path('product/cat/<slug:slug>',catagory.as_view(),name='slug')
    
]