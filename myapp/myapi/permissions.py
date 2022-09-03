from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user:
            return False
        if view.action == 'list':
            return request.user.is_authenticated and request.user.is_staff
        elif view.action == 'create':
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if not request.user:
            return False
        if not request.user.is_authenticated:
            return False
        elif view.action in ['update', 'partial_update', 'retrieve', 'destroy']:
            return obj == request.user or request.user.is_staff
        else:
            return False


class ItemPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['retrieve', 'list']:
            return True
        else:
            if request.user.is_authenticated and request.user.is_staff:
                return True
        return False


class CartPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user:
            return False
        if view.action == 'list':
            return request.user.is_authenticated and request.user.is_staff
        elif view.action == 'create':
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if not request.user:
            return False
        if not request.user.is_authenticated:
            return False
        elif view.action in ['update', 'partial_update', 'retrieve', 'destroy']:
            return obj.user == request.user or request.user.is_staff
        else:
            return False
