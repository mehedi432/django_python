from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Cardigan


class CardiganListView(ListView):
    template_name = 'various/index.html'
    model = Cardigan

class CardiganDetailView(DetailView):
    template_name = 'various/details.html'
    model = Cardigan