# realestate/permissions.py
from rest_framework.permissions import BasePermission
from users.models import User

class IsAgentOrLandlord(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [User.Role.AGENT, User.Role.LANDLORD]

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in ["GET", "HEAD", "OPTIONS"] or obj.created_by == request.user
