from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "MEEK | PRESENTER"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('kids/', include('kids.urls')),
    path('men/', include('men.urls')),
    path('women/', include('women.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
