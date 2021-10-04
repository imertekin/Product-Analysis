
from rest_framework import generics,filters, mixins
from rest_framework.response import Response
from rest_framework.views import APIView


from api.models import Product
from api.serializers import ProductSerializer, UserSerializer









# Unique Product List View 

class ProductListView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name','categoryname','brand']
    ordering_fields = '__all__'


    def get_queryset(self):
        queryset=self.queryset
        queryset=queryset.order_by('P_id','-addedtime').distinct('P_id')
        return queryset



# Single Product list for all time.

class ProductDetailView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    
    def get_queryset(self):
        queryset=self.queryset
        
        queryset=queryset.filter(P_id=self.kwargs['P_id'])
    
        return queryset



# Category Slug View
class catagory(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name','categoryname','brand']
    ordering_fields = '__all__'
    def get_queryset(self):
        queryset=self.queryset
        
        queryset=queryset.filter(slug=self.kwargs['slug'])
        

        return queryset



#Listed all product (with Duplicated)
class ProductListAdminView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name','categoryname','brand']
    ordering_fields = '__all__'

    

# CRUD Operations
class ProductDetailAdminView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


# class Register(APIView):

#     def post(self,request):

#         serializer=UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)



