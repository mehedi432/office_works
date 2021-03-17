# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category
from django.db.models import Q


# Create your views here.
class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class CategoryListView(ListView):
    model = Category
    extra_context = Product.objects.all()
    template_name = 'product/category_list.html'


class CategoryDetailView(DetailView):
    model = Category


# Search from navbar
class SearchResultView(ListView):
    model = Product
    template_name = 'product/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(style_name__icontains=query) | Q(composition__icontains=query) |
            Q(buyer_name_cleaned__icontains=query) | Q(merchant_name_cleaned__icontains=query) |
            Q(description__icontains=query) | Q(gauge__icontains=query) | Q(season__icontains=query) |
            Q(order_no__icontains=query) | Q(lc_or_pi__icontains=query)
        )

        return object_list
