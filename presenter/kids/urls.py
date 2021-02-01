from django.urls import path
from .views import KidsCategoryListView, KidsCategoryDetailView, KidsCardiganListView, KidsCardiganDetailView, KidsPulloverListView, KidsPulloverDetailView, KidsVestListView, KidsVestDetailView

app_name = 'kids' 
urlpatterns = [
    path('category/', KidsCategoryListView.as_view(), name='category-index'),
    path('category/<int:pk>/', KidsCategoryDetailView.as_view(), name='category-details'),
    
    path('category/cardigan/', KidsCardiganListView.as_view(), name='cardigan-index'),
    path('category/cardigan/<int:pk>/', KidsCardiganDetailView.as_view(), name='cardigan-details'),

    path('category/pullover/', KidsPulloverListView.as_view(), name='pullover-index'),
    path('category/pullover/<int:pk>/', KidsPulloverDetailView.as_view(), name='pullover-details'),

    path('category/vest/', KidsVestListView.as_view(), name='vest-index'),
    path('category/vest/<int:pk>/', KidsVestDetailView.as_view(), name='vest-details'),
]