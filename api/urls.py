from django.urls import path
from django.urls.conf import include




from api.views import ProductDetailView, ProductListView, catagory, test, testDetail
# from api.views import Register


urlpatterns = [

    path('product/',ProductListView.as_view(),name='Product-List'),
    path('product/<int:pk>',ProductDetailView.as_view(),name='Product-Detail'),
    # path('register/',Register.as_view(),name='Register'),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('test/',test.as_view(),name='test'),
    path('test/<int:P_id>',testDetail.as_view(),name='testdetail'),
    path('test/cat/<slug:slug>',catagory.as_view(),name='slug')
    
]