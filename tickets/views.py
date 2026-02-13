from django.shortcuts import redirect, render, get_object_or_404
from .models import Ticket
from .forms import TicketForm
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return HttpResponse("ServiceDesk is running ✅")

def ticket_list(request):
    q = request.GET.get("q", "").strip()
    status = request.GET.get("status", "").strip()

    tickets = Ticket.objects.all()

    if q:
        tickets = tickets.filter(
            Q(title__icontains=q) | Q(description__icontains=q)
        )

    if status:
        tickets = tickets.filter(status=status)

    tickets = tickets.order_by("-created_at")

    context = {
        "tickets": tickets,
        "q": q,
        "status": status,
        "status_choices": Ticket.Status.choices,
    }
    return render(request, "tickets/ticket_list.html", context)


def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, "tickets/ticket_detail.html", {"ticket": ticket})

@login_required
def ticket_create(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            return redirect("ticket_detail", ticket_id=ticket.id)
    else:
        form = TicketForm()

    return render(request, "tickets/ticket_form.html", {"form": form})


@login_required
def ticket_update(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect("ticket_detail", ticket_id=ticket.id)
    else:
        form = TicketForm(instance=ticket)

    return render(request, "tickets/ticket_form.html", {"form": form, "ticket": ticket, "mode": "edit"})


@login_required
def ticket_delete(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == "POST":
        ticket.delete()
        return redirect("ticket_list")

    return render(request, "tickets/ticket_confirm_delete.html", {"ticket": ticket})
