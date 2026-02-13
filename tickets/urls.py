from django.urls import path
from .views import ticket_list, ticket_detail, ticket_create

urlpatterns = [
    path("tickets/", ticket_list, name="ticket_list"),
    path("tickets/new/", ticket_create, name="ticket_create"),
    path("tickets/<int:ticket_id>/", ticket_detail, name="ticket_detail"),
]