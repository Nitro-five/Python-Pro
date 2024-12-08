# my_custom_app/permissions.py
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешает доступ только владельцу объекта, или только на чтение.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешить только чтение (GET) для всех
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешить изменения (POST, PUT, DELETE) только владельцу
        return obj.user == request.user
