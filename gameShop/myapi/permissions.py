from rest_framework.permissions import IsAdminUser, SAFE_METHODS

#this class was implemented to check if user is admin, if not read only permission granted

class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin

class AdminReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS and is_admin

class ReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
