from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls', namespace='main')),
    path('admin/', admin.site.urls),
    path('api/', include('devices.urls')),
    path('account/', include('accounts.urls', namespace='accounts')),
] \
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
