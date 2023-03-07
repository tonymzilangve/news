from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
EDIT_METHODS = ("PUT", "PATCH")


class AuthorAllStaffAll(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user.is_staff:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.author == request.user:
            return True

        return False


# for comments
class AuthorAllStaffAllButEdit(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.user.is_staff and request.method not in EDIT_METHODS:
            return True

        if request.method not in EDIT_METHODS:
            return True

        if obj.author == request.user:
            return True

        if obj.news.author == request.user and request.method not in EDIT_METHODS:
            return True


