# store/urls.py

from django.urls import path
from ecommerce.store.views import index
#from .views import CategoryListCreateView, ProductListCreateView

urlpatterns = [
   #path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    #path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path("", index),
]
