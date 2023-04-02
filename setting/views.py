from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Setting

# Create your views here.

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