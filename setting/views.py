from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .models import Setting

@login_required(login_url='/')
def home(request):
    current_user = request.user
    user_setting = Setting.objects.get(user_id=current_user.id)
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
def edit(request):
    current_user = request.user
    user_setting = Setting.objects.get(user_id=current_user.id)
    parentname = "avatar"
    if user_setting.parent_id != 0:
        parent = Setting.objects.get(user_id=user_setting.parent_id)
        parentname = parent.firstname + " " + parent.middlename + " " + parent.lastname
    context = {
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
    setting.save()
    return HttpResponseRedirect(reverse('setting-home'))
