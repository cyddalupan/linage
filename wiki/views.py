from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

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

def wiki_search(request):
    query = request.GET.get('search', '')
    wiki_folders = WikiFolder.objects.filter(name__icontains=query.lower())
    wikis = WikiContent.objects.filter(
        Q(title__icontains=query.lower()) |
        Q(content__icontains=query.lower())
    )
    context = {
        'wiki_folders': wiki_folders,
        'wikis': wikis
    }
    return render(request, 'wiki/wiki_home.html', context)

def wiki_page(request, wiki_id):
    wiki = WikiContent.objects.get(pk=wiki_id)
    context = {
        'wiki': wiki,
    }
    return render(request, 'wiki/wiki_single.html', context)
