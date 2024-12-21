from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'store/index.html')
# store/views.py

""" from rest_framework import generics, permissions
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

# Create your views here.
 """