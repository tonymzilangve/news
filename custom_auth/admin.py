from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserConfig(UserAdmin):
    model = CustomUser
    list_display = ('id', 'email', 'user_name', 'registered', 'is_admin', 'is_active')
    list_display_links = ('id', 'email', 'user_name',)
    search_fields = ('user_name',)
    list_filter = ('is_admin', 'is_active', )
    ordering = ('-registered',)

    fieldsets = (
        (None, {'fields': ('email', 'user_name')}),
        ('Permissions', {'fields': ('is_admin', 'is_active')})
    )


admin.site.register(CustomUser, CustomUserConfig)
