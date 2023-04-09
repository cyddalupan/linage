from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.wiki_home, name='wiki home'),
    path('folder/<int:folder_id>/', views.wiki_folder, name='wiki folder'),
    path('search/', views.wiki_search, name='wiki search'),
    path('edit/<int:wiki_id>/', views.wiki_edit, name='wiki edit'),
    path('page/<int:wiki_id>/', views.wiki_page, name='wiki page'),
    path('update/<int:wiki_id>/', views.wiki_update, name='wiki update'),
    path('create/<int:folder_id>/', views.wiki_create, name='wiki create'),
    path('insert/', views.wiki_insert, name='wiki insert'),
    path('delete/<int:wiki_id>/', views.wiki_delete, name='wiki delete'),
    path('folder-create/<int:folder_id>', views.folder_create, name="folder create"),
    path('folder-edit/<int:folder_id>', views.folder_edit, name='folder edit'),
    path('folder-delete/<int:folder_id>', views.folder_delete, name='folder delete')
]