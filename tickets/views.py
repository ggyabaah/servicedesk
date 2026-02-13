from django.shortcuts import render, get_object_or_404
from .models import Ticket

def ticket_list(request):
    tickets = Ticket.object.all().order_by("-created_at")
    return render(request, "tickets/tickets_list.html", {"tickets": tickets})


def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, "tickets/ticket_detail.html", {"ticket": ticket})


# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("ServiceDesk is running ✅")
