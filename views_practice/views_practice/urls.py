from django.contrib import admin
from django.urls import path, include


admin.site.site_header = 'View | Configuration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('various.urls')),
]
