from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


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
class AuthorAllStaffAllButEdit(AuthorAllStaffAll):

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):

        if request.user.is_staff and request.method not in self.edit_methods:
            return True

        # check author has PUT & PATCH

