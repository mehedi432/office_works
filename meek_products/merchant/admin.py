from django.contrib import admin
from .models import Merchant


# Register your models here.
@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    pass