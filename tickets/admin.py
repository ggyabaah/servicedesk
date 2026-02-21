from django.contrib import admin
from .models import Ticket
from .models import Ticket, TicketComment

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "priority", "created_at", "updated_at")
    list_filter = ("status", "priority", "created_at")
    search_fields = ("title", "description")
    ordering = ("-created_at",)

@admin.register(TicketComment)
class TicketCommentAdmin(admin.ModelAdmin):
    list_display = ("id", "ticket", "author", "created_at")
    search_fields = ("message",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)