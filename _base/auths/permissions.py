# permissions.py
from rest_framework.permissions import BasePermission
from users.models import User


class IsAgent(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_agent


class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_client


class IsLandlord(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_landlord


class IsAgentOrLandlord(BasePermission):
    """
    Custom permission to only allow agents or landlords to create or modify listings.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [User.Role.AGENT, User.Role.LANDLORD]