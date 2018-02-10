from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
    }
    return render(request, 'maps/index.html', context)


def map(request):
    context = {
    }
    return render(request, 'maps/map.html', context)
