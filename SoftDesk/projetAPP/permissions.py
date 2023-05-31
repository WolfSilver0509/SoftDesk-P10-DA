from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        """ lecture seule """
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """ Je peut intéragir avec l'objet """
        if obj.author_user_id == request.user:
            return True
        return False

