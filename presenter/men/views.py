from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Category, Cardigan, Pullover, Vest


# Create your views here.
class MenCategoryListView(ListView):
    model = Category


class MenCardiganListView(ListView):
    model = Cardigan


class MenCardiganDetailView(DetailView):
    model = Cardigan


class MenPulloverListView(ListView):
    model = Pullover


class MenPulloverDetailView(DetailView):
    model = Pullover


class MenVestListView(ListView):
    model = Vest


class MenVestDetailView(DetailView):
    model = Vest
