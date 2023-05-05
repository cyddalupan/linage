from django.urls import path

from . import views

urlpatterns = [
    path('approval/', views.wiki_approval, name='wiki_approval'),
    path('review/<int:archive_id>/', views.wiki_review, name='wiki_review'),
    path('accept-review/<int:archive_id>/', views.wiki_accept_review, name='wiki_accept_review'),
    path('reject-review/<int:archive_id>/', views.wiki_reject_review, name='wiki_reject_review'),
    path('home/', views.wiki_home, name='wiki home'),
    path('folder/<int:folder_id>/', views.wiki_folder, name='wiki folder'),
    path('search/', views.wiki_search, name='wiki search'),
    path('page/<int:wiki_id>/', views.wiki_page, name='wiki page'),
    path('edit/<int:wiki_id>/', views.wiki_edit, name='wiki edit'),
    path('create/<int:folder_id>/', views.wiki_create, name='wiki create'),
    path('delete/<int:wiki_id>/', views.wiki_delete, name='wiki delete'),
    path('folder-create/<int:folder_id>', views.folder_create, name="folder create"),
    path('folder-edit/<int:folder_id>', views.folder_edit, name='folder edit'),
    path('folder-delete/<int:folder_id>', views.folder_delete, name='folder delete'),
    path('email', views.send_email, name='send email')
]
