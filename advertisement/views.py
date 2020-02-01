from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ad_page(request):
    return HttpResponse('Страница обьявления!')