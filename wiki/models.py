from django.db import models
from django.forms import ModelForm

class WikiFolder(models.Model):
    name = models.CharField(unique=True, max_length=255)
    folder_id = models.IntegerField()
    created_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
class WikiFolderForm(ModelForm):
    class Meta:
        model = WikiFolder
        fields = ["name"]

class WikiContent(models.Model):
    title = models.CharField(unique=True, max_length=255)
    content = models.TextField()    
    folder = models.ForeignKey(WikiFolder, on_delete=models.CASCADE, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class WikiContentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["folder"].choices = [(folder.id, folder.name) for folder in WikiFolder.objects.all()]

    class Meta:
        model = WikiContent
        fields = ["title", "content", "folder"]

class WikiContentArchive(models.Model):
    title = models.CharField(unique=True, max_length=255)
    content = models.TextField()    
    folder = models.ForeignKey(WikiFolder, on_delete=models.CASCADE, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
