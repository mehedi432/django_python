from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Category, Cardigan, Pullover, Vest


# Create your views here.
class WomenCategoryListView(ListView):
    model = Category


class WomenCardiganListView(ListView):
    model = Cardigan


class WomenCardiganDetailView(DetailView):
    model = Cardigan


class WomenPulloverListView(ListView):
    model = Pullover


class WomenPulloverDetailView(DetailView):
    model = Pullover


class WomenVestListView(ListView):
    model = Vest


class WomenVestDetailView(DetailView):
    model = Vest
