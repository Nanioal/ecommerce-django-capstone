# store/urls.py

from django.urls import path
from .views import ProductListCreate, ProductRetrieveUpdateDestroy
from django.urls import path
from .views import index
from . import views


urlpatterns = [
    path('products/', views.ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-retrieve-update-destroy'),
    path('', index, name='index'),
]

    

