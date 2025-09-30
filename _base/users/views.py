# views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from auths.permissions import IsAgent, IsClient, IsLandlord


class AgentDashboardView(APIView):
    permission_classes = [IsAgent]

    def get(self, request):
        return Response({"message": "Welcome to the Agent Dashboard"})


class ClientDashboardView(APIView):
    permission_classes = [IsClient]

    def get(self, request):
        return Response({"message": "Welcome to the Client Dashboard"})


class LandlordDashboardView(APIView):
    permission_classes = [IsLandlord]

    def get(self, request):
        return Response({"message": "Welcome to the Landlord Dashboard"})
