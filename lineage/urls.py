"""lineage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from wiki import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # WIKI
    path('wiki-home/', views.wiki_home, name='wiki home'),
    path('wiki-folder/<int:folder_id>/', views.wiki_folder, name='wiki folder'),
    path('wiki-search/', views.wiki_search, name='wiki search'),
    path('wiki-edit/<int:wiki_id>/', views.wiki_edit, name='wiki edit'),
    path('wiki-page/<int:wiki_id>/', views.wiki_page, name='wiki page'),
    path('wiki-update/<int:wiki_id>/', views.wiki_update, name='wiki update'),
    path('wiki-create/', views.wiki_create, name='wiki create'),
    path('wiki-insert/', views.wiki_insert, name='wiki insert'),
    path('wiki-delete/<int:wiki_id>/', views.wiki_delete, name='wiki delete'),
]
