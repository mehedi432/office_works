from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from django.db.models import Q


# Create your views here.
class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


def category_list(request, pk):
    if pk == 1:
        context = {
            'products': Product.objects.filter(Q(category__icontains='pullover'))
        }
        return render(request, 'category/category_list.html', context)

    elif pk == 2:
        context = {
            'products': Product.objects.filter(Q(category__icontains='cardigan'))
        }
        return render(request, 'category/category_list.html', context)

    elif pk == 3:
        context = {
            'products': Product.objects.filter(Q(category__icontains='vest'))
        }
        return render(request, 'category/category_list.html', context)
    else:
        return render(request, 'category/category_list.html')


def gender_list(request, pk):
    if pk == 1:
        context = {
            'products': Product.objects.filter(Q(gender__icontains='male'))
        }
        return render(request, 'category/category_list.html', context)

    elif pk == 2:
        context = {
            'products': Product.objects.filter(Q(gender__icontains='female'))
        }
        return render(request, 'category/category_list.html', context)

    elif pk == 3:
        context = {
            'products': Product.objects.filter(Q(gender__icontains='kids'))
        }
        return render(request, 'category/category_list.html', context)

    else:
        return render(request, 'category/category_list.html')


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
