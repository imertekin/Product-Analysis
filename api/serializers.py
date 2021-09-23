
from django.contrib.auth.models import User
from django.db.models.fields import Field
from rest_framework import fields, serializers
from api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    
    addedtime=serializers.ReadOnlyField()
    addedtime=serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model=Product
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['username','email','password']