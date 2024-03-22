from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = 'You are not a owner!'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False