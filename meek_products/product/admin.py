from django.contrib import admin
from .models import Product
from django.utils.html import format_html


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('style_name', 'description', 'composition', 'lc_or_pi', 'buyer_name_cleaned',
                     'merchant_name_cleaned', 'fob', 'moq')
    list_display = ('style_name', 'description', 'composition', 'merchant_name_cleaned', 'buyer_name',
                    'date_shipment', 'shipment_quantity', 'lc_or_pi', 'image', 'fob', 'moq')
    list_display_links = ('style_name', 'description')
    list_filter = ()
    list_per_page = 21

    @staticmethod
    def image(obj):
        return format_html('<img src="{0}" style="width: 55px; height:55px;" />'.format(obj.image_primary.url))
