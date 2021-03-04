from django.urls import path
from .views import index, about

urlpatterns = [
    path("", index, name='page-index'),
    path("about/", about, name="page-about")
]