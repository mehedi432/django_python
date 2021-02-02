from django.urls import path
from .views import WomenCategoryListView,WomenCardiganListView, WomenCardiganDetailView, WomenPulloverListView, WomenPulloverDetailView, WomenVestListView, WomenVestDetailView

app_name='women'
urlpatterns = [
    path('category/', WomenCategoryListView.as_view(), name='women-category'),

    path('category/cardigan/', WomenCardiganListView.as_view(), name='women-index'),
    path('category/cardigan/<int:pk>', WomenCardiganDetailView.as_view(), name='women-details'),

    path('category/pullover/', WomenPulloverListView.as_view(), name='women-index'),
    path('category/pullover/<int:pk>', WomenPulloverDetailView.as_view(), name='women-details'),

    path('category/pullover/', WomenVestListView.as_view(), name='vest-index'),
    path('category/pullover/<int:pk>', WomenVestDetailView.as_view(), name='vest-details')   
]