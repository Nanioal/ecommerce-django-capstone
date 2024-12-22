# store/models.py

from django.db import models

class Product(models.Model):
    name= models.CharField(max_length= 50)
    description=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    catagory= models.CharField(max_length=50)
    stock_quantity = models.IntegerField()
    image_url = models.URLField(max_length=200) 
    created_date = models.DateTimeField(auto_now_add=True) 
def __str__(self): return self.name
