from django.contrib import admin
from .models import Product, Category, Gender
from django.utils.html import format_html


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('style_name', 'description', 'composition', 'fob', 'moq', 'lc_or_pi', 'buyer_name')
    list_display = ('id', 'style_name', 'description', 'composition', 'fob', 'moq', 'merchant_name', 'buyer_name',
                    'date_shipment', 'shipment_quantity', 'lc_or_pi', 'image')
    list_display_links = ('id', 'style_name')
    list_filter = ()
    list_per_page = 21

    def image(self, obj):
        return format_html('<img src="{0}" style="width: 45px; height:45px;" />'.format(obj.image_primary.url))


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    pass
