from django.db import models

# Create your models here.
class categorydb(models.Model):
    category = models.CharField(max_length=30, null=True, blank=True)
    descriptions = models.CharField(max_length=20, null=True, blank=True)
    category_img = models.ImageField(upload_to="profile", null=True, blank=True)
class productdb(models.Model):
    Category = models.CharField(max_length=30, null=True, blank=True)
    Product_name = models.CharField(max_length=20, null=True, blank=True)
    Price = models.CharField(max_length=20, null=True, blank=True)
    Description = models.CharField(max_length=20, null=True, blank=True)
    Brand = models.CharField(max_length=20, null=True, blank=True)
    product_img = models.ImageField(upload_to="profile", null=True, blank=True)