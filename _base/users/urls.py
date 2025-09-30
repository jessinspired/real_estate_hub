from django.urls import path
from users.views import AgentDashboardView, ClientDashboardView, LandlordDashboardView

urlpatterns = [
    path("dashboard/agent/", AgentDashboardView.as_view(),
         name="agent_dashboard"),
    path("dashboard/client/", ClientDashboardView.as_view(),
         name="client_dashboard"),
    path("dashboard/landlord/", LandlordDashboardView.as_view(),
         name="landlord_dashboard"),
]
