from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='setting-home'),
    path('new/', views.new, name='setting-new'),
    path('edit/', views.edit, name='setting-edit'),
    path('update/<int:setting_id>/', views.update, name='setting-update'),
]