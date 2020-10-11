from django.db import models

class Product_5(models.Model):
    username = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    database_name = models.CharField(max_length=250)
    
    class Meta:

        app_label = 'product5'