from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 

from .models import Category, Cardigan, Pullover, Vest


# Create your views here.
class KidsCategoryListView(ListView):
    model = Category


class KidsCategoryDetailView(DetailView):
    model = Category


class KidsCardiganListView(ListView):
    model = Cardigan


class KidsCardiganDetailView(DetailView):
    model = Cardigan


class KidsPulloverListView(ListView):
    model = Pullover


class KidsPulloverDetailView(DetailView):
    model = Pullover


class KidsVestListView(ListView):
    model = Vest


class KidsVestDetailView(DetailView):
    model = Vest