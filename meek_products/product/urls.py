from django.urls import path
from .views import ProductListView, ProductDetailView, SearchResultView,\
    CategoryListView, CategoryDetailView

app_name = 'product'
urlpatterns = [
    path("", ProductListView.as_view(), name='product-list'),
    path("<int:pk>/", ProductDetailView.as_view(), name='product-detail'),
    path("search/", SearchResultView.as_view(), name='search'),

    path("category/", CategoryListView.as_view(), name='category-index'),
    path("category/<int:pk>", CategoryDetailView.as_view(), name='category-details'),
]
