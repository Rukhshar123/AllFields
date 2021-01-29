from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    cat_id =  models.ForeignKey(Category,on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now=True, null=False)
    stock = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    cat_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_id = models.ForeignKey(SubCategory,on_delete=models.CASCADE)





