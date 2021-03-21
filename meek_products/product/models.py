from django.db import models
from merchant.models import Merchant
from buyer.models import Buyer

CATEGORY_CHOICES = (('pullover', 'Pullover'), ('cardigan', 'Cardigan'), ('vest', 'Vest'))
GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'), ('kids', 'Kids'))


# Create your models here.
class Product(models.Model):

    style_name = models.CharField(max_length=34)

    merchant_name = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    buyer_name = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    buyer_name_cleaned = models.CharField(max_length=55, help_text="Please, write the email of buyer")
    merchant_name_cleaned = models.CharField(max_length=55, help_text="Please, write the email of associate merchant")

    gender = models.CharField(max_length=21, choices=GENDER_CHOICES)
    category = models.CharField(max_length=21, choices=CATEGORY_CHOICES)

    image_primary = models.ImageField(default='default.jpg', upload_to="media/product")
    image_secondary = models.ImageField(default='default.jpg', upload_to="media/product", blank=True)
    image_extra = models.ImageField(default='default.jpg', upload_to="media/product", blank=True)
    image_chart = models.ImageField(default='default.jpg', upload_to="media/chart", blank=True)

    description = models.CharField(max_length=34)
    composition = models.CharField(max_length=55)
    gauge = models.CharField(max_length=13)
    size = models.CharField(max_length=13)
    weight = models.CharField(max_length=89)
    time = models.CharField(max_length=21)
    moq = models.CharField(max_length=21, blank=True, null=True)
    fob = models.PositiveIntegerField(blank=True, null=True)
    date_order = models.DateField(auto_now_add=False)
    date_shipment = models.DateField(auto_now_add=False)

    season = models.CharField(max_length=21)
    order_no = models.CharField(max_length=34)
    lc_or_pi = models.CharField(max_length=55)
    shipment_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.style_name

