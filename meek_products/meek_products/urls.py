from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


admin.site.site_title = "Meek Sweater"
admin.site.index_title = "Welcome to Meek's Product Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
