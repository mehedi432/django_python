from django.urls import path
from .views import CardiganListView, CardiganDetailView


urlpatterns = [
    path('', CardiganListView.as_view(), name='index'),
    path('cardigan/<pk>/', CardiganDetailView.as_view(), name='cardigan-details')
]