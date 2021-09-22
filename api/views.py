from rest_framework import generics,filters
from rest_framework.response import Response
from rest_framework.views import APIView


from api.models import Product
from api.serializers import ProductSerializer, UserSerializer
from django.contrib.auth.models import User



class ProductListView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','categoryname','brand']


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


class Register(APIView):

    def post(self,request):

        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



