from django.urls import path
from django.urls import path, include
from .views import ticket_list, ticket_detail, ticket_create, ticket_update, ticket_delete

urlpatterns = [
    path("tickets/", ticket_list, name="ticket_list"),
    path("tickets/new/", ticket_create, name="ticket_create"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("tickets/<int:ticket_id>/", ticket_detail, name="ticket_detail"),
    path("tickets/<int:ticket_id>/edit/", ticket_update, name="ticket_update"),
    path("tickets/<int:ticket_id>/delete/", ticket_delete, name="ticket_delete"),
]   