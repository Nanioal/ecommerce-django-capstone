from rest_framework import serializers
from .models import Product, Category
from rest_framework import serializers
from .models import User, Product, Category, Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'stock_quantity', 'image_url']
class ReviewSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Review 
        fields = ['id', 'product', 'user', 'rating', 'comment', 'created_date'] 
        read_only_fields = ['user', 'created_date']