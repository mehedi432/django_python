from django.urls import path
from .views import MenCategoryListView, MenCardiganListView, MenCardiganDetailView, MenPulloverListView,MenPulloverDetailView, MenVestListView, MenVestDetailView


app_name="men"
urlpatterns = [
    path('category/', MenCategoryListView.as_view(), name='category-index'),

    path('category/cardigan/', MenCardiganListView.as_view(), name='cardigan-index'),
    path('category/cardigan/<int:pk>/', MenCardiganDetailView.as_view(), name='cardigan-details'),

    path('category/pullover/', MenPulloverListView.as_view(), name='pullover-index'),
    path('category/pullover/<int:pk>', MenPulloverDetailView.as_view(), name='pullover-details'),
    
    path('category/vest/', MenVestListView.as_view(), name='vest-index'),
    path('category/vest/<int:pk>', MenVestDetailView.as_view(), name='vest-details'),
]