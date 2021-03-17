from django.db import models
from merchant.models import Merchant


# Create your models here.
class Buyer(models.Model):
    full_name = models.CharField(max_length=34)
    email_address = models.EmailField()
    buying_house = models.CharField(max_length=55)
    first_order = models.DateField(auto_now_add=False)
    last_order = models.DateField(auto_now_add=False)
    phone_number = models.CharField(max_length=21)
    associate_merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
