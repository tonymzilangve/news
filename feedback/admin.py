from django.contrib import admin
from .models import *


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'timestamp')
    list_display_links = ('id', 'author', )
    search_fields = ('author',)
    list_filter = ('author', )
    ordering = ('-timestamp',)


admin.site.register(Comment, CommentAdmin)
