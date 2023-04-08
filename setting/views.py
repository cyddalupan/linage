from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Setting

@login_required(login_url='/')
def home(request):
    current_user = request.user
    if Setting.objects.filter(user_id=current_user.id).exists():
        user_setting = Setting.objects.get(user_id=current_user.id)
    else:
        return HttpResponseRedirect(reverse('setting-new'))
        
    parentname = "avatar"
    if user_setting.parent_id != 0:
        parent = Setting.objects.get(user_id=user_setting.parent_id)
        parentname = parent.firstname + " " + parent.middlename + " " + parent.lastname
    context = {
        'user_setting': user_setting,
        'parentname': parentname,
    }
    return render(request, 'setting/home.html', context)

@login_required(login_url='/')
def new(request):
    current_user = request.user
    setting = Setting(
        user_id=current_user.id,
        parent_id=0
    )
    setting.save()
    return HttpResponseRedirect(reverse('setting-home'))

@login_required(login_url='/')
def edit(request):
    current_user = request.user
    parents = Setting.objects.filter(~Q(user_id = current_user.id))
    user_setting = Setting.objects.get(user_id=current_user.id)
    parentname = "avatar"
    if user_setting.parent_id != 0:
        parent = Setting.objects.get(id=user_setting.parent_id)
        parentname = parent.firstname + " " + parent.middlename + " " + parent.lastname
    context = {
        'parents': parents,
        'user_setting': user_setting,
        'parentname': parentname,
    }
    return render(request, 'setting/edit.html', context)

@login_required(login_url='/')
def update(request, setting_id):
    setting = get_object_or_404(Setting, pk=setting_id)
    setting.firstname = request.POST['firstname']
    setting.middlename = request.POST['middlename']
    setting.lastname = request.POST['lastname']
    setting.birthday = request.POST['birthday']
    setting.parent_id = request.POST['parent']
    setting.save()
    return HttpResponseRedirect(reverse('setting-home'))
