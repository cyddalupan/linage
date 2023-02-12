from django.shortcuts import render
from django.http import HttpResponse

def my_view(request):
    context = {}
    return render(request, 'wiki/index.html', context)


def other_page(request):
    context = {}
    return render(request, 'wiki/other.html', context)