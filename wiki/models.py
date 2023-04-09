from django.db import models
from django.forms import ModelForm

class WikiContent(models.Model):
    title = models.CharField(unique=True, max_length=255)
    content = models.TextField()    
    folder_id = models.IntegerField()
    created_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class WikiFolder(models.Model):
    name = models.CharField(unique=True, max_length=255)
    folder_id = models.IntegerField()
    # Remove this after reference
    #temfolder = models.ForeignKey(WikiContent, on_delete=models.CASCADE)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    # @classmethod
    # def folder_update(cls, folder_id):
    #     folder_id = cls(folder_id=folder_id)
    #     # do something with the book
    #     return folder_id

    def __str__(self):
        return self.name

class WikiFolderForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['temfolder'].choices = [(folder.id, folder.title) for folder in WikiContent.objects.all()]

    class Meta:
        model = WikiFolder
        fields = ["name"]
        # Remove all comments after reference
        # fields = ["name", "folder_id", "temfolder"]

class WikiContentArchive(models.Model):
    title = models.CharField(unique=True, max_length=255)
    content = models.TextField()    
    folder_id = models.IntegerField()
    created_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
