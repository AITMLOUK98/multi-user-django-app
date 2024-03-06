from rest_framework.permissions import BasePermission

class HasFullAccess(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.userprofile.role == 'beta_player':
            return True
        return False

class HasViewAccess(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.userprofile.role in ['company_user', 'subscriber']:
            return True
        return False
