from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # Includes URLs from pages app
    path('cars/', include('cars.urls')),  # Includes URLs from cars app
    path('accounts/', include('accounts.urls')),  # Includes URLs from accounts app
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
