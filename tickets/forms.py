from django import forms
from .models import Ticket
from .models import TicketComment

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "status", "priority"]


class TicketCommentForm(forms.ModelForm):
    class Meta:
        model = TicketComment
        fields = ["message"]