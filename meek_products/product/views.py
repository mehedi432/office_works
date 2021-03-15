# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from django.db.models import Q


# Create your views here.
class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


# Search from navbar
class SearchResultView(ListView):
    model = Product
    template_name = 'product/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(style_name__icontains=query) | Q(composition__icontains=query) | Q(merchant__merchant_name__icontains=query),
            Q(buyer_name__buyer_name__icontains=query) | Q(buyer_name_cleaned__icontains=query)
        )

        return object_list
