
from rest_framework import generics,filters, mixins
from rest_framework.response import Response
from rest_framework.views import APIView


from api.models import Product
from api.serializers import ProductSerializer, UserSerializer








class ProductListView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','categoryname','brand']

    


        

class testDetail(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def get_queryset(self):
        queryset=self.queryset
        
        queryset=queryset.filter(P_id=self.kwargs['P_id'])
    
        return queryset


class test(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=P_id']


    def get_queryset(self):
        queryset=self.queryset
        queryset=queryset.order_by('P_id','-addedtime').distinct('P_id')
        return queryset



        
class catagory(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    def get_queryset(self):
        queryset=self.queryset
        
        queryset=queryset.filter(slug=self.kwargs['slug'])
        

        return queryset
    

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


# class Register(APIView):

#     def post(self,request):

#         serializer=UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)



