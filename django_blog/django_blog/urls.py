from django.contrib import admin
from django.urls import path, include

from users import views as users_views


admin.site.site_header = "Dellab | Blog"
admin.site.site_title = "Dellab | A place for learners"
admin.site.index_title = "Dellab For Learners"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('register/', users_views.register, name='register')
]
