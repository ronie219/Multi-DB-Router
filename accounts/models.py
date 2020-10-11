from django.db import models
from django.contrib.auth.models import User

class CustumUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    database1 = models.BooleanField(default=True)
    database2 = models.BooleanField(default=False)
    database3 = models.BooleanField(default=False)
    database4 = models.BooleanField(default=False)
    database5 = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username



class Product_1(models.Model):
    username = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    database_name = models.CharField(max_length=250)

