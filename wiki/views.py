from django.forms import modelform_factory, modelformset_factory
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import WikiContent, WikiContentForm, WikiFolder, WikiFolderForm

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

        if folder.folder_id == 0:
            break

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
    wiki = get_object_or_404(WikiContent, pk=wiki_id)
    if request.method == 'POST':
        formset = WikiContentForm(request.POST, instance=wiki)
        if formset.is_valid():
            wiki = formset.save(commit=False)
            wiki.save()
            return HttpResponseRedirect(reverse('wiki page', args=(wiki.id,)))
    else:
        formset = WikiContentForm(instance=wiki)
    wiki_folders = WikiFolder.objects.all()
    context = {
        'wiki': wiki,
        'wiki_folders':wiki_folders,
        'formset': formset
    }
    return render(request, 'wiki/wiki_edit.html', context)

@login_required(login_url='/')
def wiki_create(request, folder_id):
    if request.method == 'POST':
        formset = WikiContentForm(request.POST)
        if formset.is_valid():
            wiki = formset.save(commit=False)
            wiki.created_by = 0
            wiki.updated_by = 0
            wiki.save()
            return HttpResponseRedirect(reverse('wiki folder', args=[wiki.folder.id] ))
    else:
        formset = WikiContentForm(initial={'folder': folder_id})
    wiki_folders = WikiFolder.objects.all()
    context = {
        'wiki_folders' : wiki_folders,
        'folder_id' : folder_id,
        'formset' : formset,
    }
    return render(request, 'wiki/wiki_create.html', context)

@login_required(login_url='/')
def wiki_delete(request, wiki_id):
    wiki = get_object_or_404(WikiContent, pk=wiki_id)
    wiki.delete()
    return HttpResponseRedirect(reverse('wiki home'))

@login_required(login_url='/')
def folder_create(request, folder_id):
    if request.method == 'POST':
        formset = WikiFolderForm(request.POST)
        if formset.is_valid():
            folder = formset.save(commit=False)
            folder_id:int = int(request.POST['folder'])
            folder.folder_id = folder_id
            folder.created_by = 0
            folder.updated_by = 0
            folder.save()
            return HttpResponseRedirect(reverse('wiki folder', args=[folder.folder_id] ))
    else:
        formset = WikiFolderForm()

    wiki_folders = WikiFolder.objects.all()

    context = {
        'wiki_folders':wiki_folders,
        'folder_id':folder_id,
        "formset": formset,
    }
    return render(request, 'wiki/folder_create.html', context)

@login_required(login_url='/')
def folder_edit(request, folder_id):
    folder = get_object_or_404(WikiFolder, pk=folder_id)
    
    if request.method == 'POST':
        formset = WikiFolderForm(request.POST, instance=folder)
        if formset.is_valid():
            folder = formset.save(commit=False)
            folder_id:int = int(request.POST['folder'])
            folder.folder_id = folder_id
            folder.created_by = 0
            folder.updated_by = 0
            folder.save()
            return HttpResponseRedirect(reverse('wiki folder', args=[folder.folder_id] ))
    else:
        formset = WikiFolderForm(instance=folder)

    wiki_folders = WikiFolder.objects.all()

    context = {
        'wiki_folders':wiki_folders,
        'current':folder,
        "formset": formset,
    }
    return render(request, 'wiki/folder_edit.html', context)

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