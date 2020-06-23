from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User



class conccurent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    date = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
    	return"{}-{}-{}".format(self.name,self.date,self.url)
class config(models.Model):
	keywords=models.CharField(max_length=200)
	date=models.DateTimeField(auto_now_add=True)
	everyday=models.BooleanField(default=True)
	everyweek=models.BooleanField(default=False)
	everymonth=models.BooleanField(default=False)


# Create your models here.
