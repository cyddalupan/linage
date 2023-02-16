from django.shortcuts import render
from django.http import HttpResponse

from .models import WikiContent, WikiFolder

def my_view(request):
    context = {}
    return render(request, 'wiki/index.html', context)


def other_page(request):
    context = {}
    return render(request, 'wiki/other.html', context)

def wiki_home(request):
    wiki_folders = WikiFolder.objects.filter(folder_id = 0)
    wikis = WikiContent.objects.filter(folder_id = 0)
    context = {
        'wiki_folders': wiki_folders,
        'wikis': wikis
    }
    return render(request, 'wiki/wiki_home.html', context)

def wiki_folder(request, folder_id):
    wiki_folders = WikiFolder.objects.filter(folder_id = folder_id)
    wikis = WikiContent.objects.filter(folder_id = folder_id)
    context = {
        'wiki_folders': wiki_folders,
        'wikis': wikis
    }
    return render(request, 'wiki/wiki_home.html', context)

def wiki_search(request, query):
    wiki_folders = WikiFolder.objects.filter(folder_id = 0)
    wikis = WikiContent.objects.filter(folder_id = 0)
    context = {
        'wiki_folders': wiki_folders,
        'wikis': wikis
    }
    return render(request, 'wiki/wiki_home.html', context)
