from django.db import models

# Create your models here.

class Income(models.Model):
    price = models.IntegerField(null=1,blank=1)
    text = models.CharField(max_length=200,null=1,blank=1)
    time = models.DateTimeField(null=1,blank=1)


class Expensses(models.Model):
    price = models.IntegerField(null=1, blank=1)
    text = models.CharField(max_length=200, null=1, blank=1)
    time = models.DateTimeField(null=1, blank=1)
