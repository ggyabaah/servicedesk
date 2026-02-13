from django.shortcuts import render, get_object_or_404
from .models import Ticket
from .forms import TicketForm


def ticket_list(request):
    tickets = Ticket.objects.all().order_by("-created_at")
    return render(request, "tickets/ticket_list.html", {"tickets": tickets})


def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, "tickets/ticket_detail.html", {"ticket": ticket})


# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("ServiceDesk is running ✅")


def ticket_create(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            return redirect("ticket_detail", ticket_id=ticket.id)
    else:
        form = TicketForm()

    return render(request, "tickets/ticket_form.html", {"form": form})
