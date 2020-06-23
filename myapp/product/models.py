from django.db import models



class products(models.Model):
    id = models.AutoField(primary_key=True)
    name_product = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    date = models.DateField(auto_now=False, auto_now_add=False)


# Create your models here.
