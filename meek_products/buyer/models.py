from django.db import models
from merchant.models import Merchant


# Create your models here.
class Buyer(models.Model):
    first_name = models.CharField(max_length=34)
    last_name = models.CharField(max_length=34)
    buying_house = models.CharField(max_length=55)
    first_order = models.DateField(auto_now_add=False)
    last_order = models.DateField(auto_now_add=False)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=21)
    associate_merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)

    def __str__(self):
        return self.email_address
