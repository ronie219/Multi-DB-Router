from django.db import models
from accounts.models import CustumUser

class Product_2(models.Model):
    username = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    database_name = models.CharField(max_length=250)
    
    class Meta:

        app_label = 'product2'
        