from django.urls import path
from .views import ProductListView, ProductDetailView, SearchResultView,\
    category_list, gender_list

app_name = 'product'
urlpatterns = [
    path("", ProductListView.as_view(), name='product-list'),
    path("<int:pk>/", ProductDetailView.as_view(), name='product-detail'),
    path("search/", SearchResultView.as_view(), name='search'),

    path("category/<int:pk>", category_list, name='category-index'),
    path("gender/<int:pk>", gender_list, name='gender-index'),

    # path("category/<int:pk>", CategoryDetailView.as_view(), name='category-details'),
]
