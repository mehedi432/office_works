from django.db import models


# Create your models here.
class Merchant(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    joining_date = models.DateField(auto_now_add=False)
    resign_date = models.DateField(auto_now_add=False)
    phone_number = models.CharField(max_length=21)
    email_address = models.EmailField()

    def __str__(self):
        return self.email_address
