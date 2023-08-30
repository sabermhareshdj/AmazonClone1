from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product , Brand , ProductImages , Review

# Create your views here.

class ProductList(ListView):
    model = Product         # context : object_list , model_list


class ProductDetail(DetailView):
    model = Product          # context 