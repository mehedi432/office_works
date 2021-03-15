from django.contrib import admin
from .models import Purchase


# Register your models here.
@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'quantity', 'price')


