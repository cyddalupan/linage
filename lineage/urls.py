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
    # WIKI
    path('wiki-home/', views.wiki_home, name='wiki home'),
    path('wiki-folder/<int:folder_id>/', views.wiki_folder, name='wiki folder'),
    path('wiki-search/', views.wiki_search, name='wiki search'),
    path('wiki-page/<int:wiki_id>', views.wiki_page, name='wiki page'),

    path('hello/', views.my_view, name='hello'),
    path('other/', views.other_page, name='other'),
    path('admin/', admin.site.urls),
]
