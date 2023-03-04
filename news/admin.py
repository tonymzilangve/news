from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'timestamp')
    list_display_links = ('id', 'title', 'author', )
    search_fields = ('title', 'author', )
    list_filter = ('author', )


admin.site.register(News, NewsAdmin)
