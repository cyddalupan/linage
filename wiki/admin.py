from django.contrib import admin

from wiki.models import WikiContent, WikiContentArchive, WikiFolder


admin.site.register(WikiContent)
admin.site.register(WikiFolder)
admin.site.register(WikiContentArchive)
