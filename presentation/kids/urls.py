from django.urls import path
from . import views


app_name = "kids"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:category_id>/", views.details, name="details"),
]

