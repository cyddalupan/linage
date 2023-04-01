from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import WikiContent, WikiFolder

@login_required(login_url='/')
def wiki_home(request):
    wiki_folders = WikiFolder.objects.filter(folder_id = 0)
    wikis = WikiContent.objects.filter(folder_id = 0)
    context = {
        'wiki_folders': wiki_folders,
        'wikis': wikis,
        'folder_id': 0
    }
    return render(request, 'wiki/wiki_home.html', context)

@login_required(login_url='/')
def wiki_folder(request, folder_id):
    if folder_id == 0:
        return HttpResponseRedirect(reverse('wiki home'))
    wiki_folders = WikiFolder.objects.filter(folder_id = folder_id)
    wikis = WikiContent.objects.filter(folder_id = folder_id)

    trail = {};
    loop_folder_id = folder_id
    # Get Trail
    while True: 
        folder =  WikiFolder.objects.get(id=loop_folder_id)
        loop_folder_id = folder.folder_id
        trail[folder.id] = folder.name
        print(trail)
        if folder.folder_id == 0:
            break
    print(trail)

    context = {
        'wiki_folders': wiki_folders,
        'wikis': wikis,
        'folder_id': folder_id,
        'trail': trail,
    }
    return render(request, 'wiki/wiki_home.html', context)

@login_required(login_url='/')
def wiki_search(request):
    query = request.GET.get('search', '')
    wiki_folders = WikiFolder.objects.filter(name__icontains=query.lower())
    wikis = WikiContent.objects.filter(
        Q(title__icontains=query.lower()) |
        Q(content__icontains=query.lower())
    )
    context = {
        'wiki_folders': wiki_folders,
        'wikis': wikis,
        'folder_id': 0
    }
    return render(request, 'wiki/wiki_home.html', context)

@login_required(login_url='/')
def wiki_page(request, wiki_id):
    wiki = WikiContent.objects.get(pk=wiki_id)
    context = {
        'wiki': wiki,
    }
    return render(request, 'wiki/wiki_single.html', context)

@login_required(login_url='/')
def wiki_edit(request, wiki_id):
    wiki = WikiContent.objects.get(pk=wiki_id)
    wiki_folders = WikiFolder.objects.all()
    context = {
        'wiki': wiki,
        'wiki_folders':wiki_folders
    }
    return render(request, 'wiki/wiki_edit.html', context)

@login_required(login_url='/')
def wiki_update(request, wiki_id):
    wiki = get_object_or_404(WikiContent, pk=wiki_id)
    wiki.title = request.POST['title']
    wiki.content = request.POST['content']
    wiki.folder_id = request.POST['folder']
    wiki.save()
    return HttpResponseRedirect(reverse('wiki page', args=(wiki.id,)))

@login_required(login_url='/')
def wiki_create(request, folder_id):
    wiki_folders = WikiFolder.objects.all()
    context = {
        'wiki_folders':wiki_folders,
        'folder_id':folder_id,
    }
    return render(request, 'wiki/wiki_create.html', context)

@login_required(login_url='/')
def wiki_insert(request):
    wiki = WikiContent(
        title=request.POST['title'], 
        content=request.POST['content'],
        folder_id=request.POST['folder'],
        created_by=0,
        updated_by=0
    )
    wiki.save()
    return HttpResponseRedirect(reverse('wiki folder', args=[request.POST['folder']] ))

@login_required(login_url='/')
def wiki_delete(request, wiki_id):
    wiki = get_object_or_404(WikiContent, pk=wiki_id)
    wiki.delete()
    return HttpResponseRedirect(reverse('wiki home'))

@login_required(login_url='/')
def folder_create(request, folder_id):
    wiki_folders = WikiFolder.objects.all()
    context = {
        'wiki_folders':wiki_folders,
        'folder_id':folder_id,
    }
    return render(request, 'wiki/folder_create.html', context)

@login_required(login_url='/')
def folder_create(request, folder_id):
    wiki_folders = WikiFolder.objects.all()
    context = {
        'wiki_folders':wiki_folders,
        'folder_id':folder_id,
    }
    return render(request, 'wiki/folder_create.html', context)

@login_required(login_url='/')
def folder_insert(request):
    folder = WikiFolder(
        name=request.POST['name'],
        folder_id=request.POST['folder'],
        created_by=0,
        updated_by=0
    )
    folder.save()
    return HttpResponseRedirect(reverse('wiki folder', args=[request.POST['folder']] ))

@login_required(login_url='/')
def folder_edit(request, folder_id):
    folder = get_object_or_404(WikiFolder, pk=folder_id)
    wiki_folders = WikiFolder.objects.all()
    context = {
        'wiki_folders':wiki_folders,
        'current':folder
    }
    return render(request, 'wiki/folder_edit.html', context)

@login_required(login_url='/')
def folder_update(request, folder_id):
    folder = get_object_or_404(WikiFolder, pk=folder_id)
    folder.name = request.POST['name']
    folder.folder_id = request.POST['folder']
    folder.save()
    return HttpResponseRedirect(reverse('wiki folder', args=[request.POST['folder']]))

@login_required(login_url='/')
def folder_delete(request, folder_id):
    folder = get_object_or_404(WikiFolder, pk=folder_id)
    parent_folder_id = folder.folder_id
    folders_inside = WikiFolder.objects.filter(folder_id=folder_id)
    wikis_inside = WikiContent.objects.filter(folder_id=folder_id)
    total_files = len(folders_inside)+len(wikis_inside)
    if total_files == 0:
        folder.delete()
        return HttpResponseRedirect(reverse('wiki folder', args=[parent_folder_id]))
    messages.error(request, 'You can only delete an empty folder')
    return HttpResponseRedirect(reverse('wiki folder', args=[folder_id]))