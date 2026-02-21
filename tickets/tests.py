from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Ticket

User = get_user_model()


class TicketPermissionsTests(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username="owner", password="pass12345")
        self.other = User.objects.create_user(username="other", password="pass12345")

        self.ticket = Ticket.objects.create(
            title="Owner ticket",
            description="Test",
            owner=self.owner,
            status=Ticket.Status.OPEN,
            priority=Ticket.Priority.MEDIUM,
        )

    def test_create_requires_login(self):
        url = reverse("ticket_create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # redirect to login

    def test_owner_can_edit(self):
        self.client.login(username="owner", password="pass12345")
        url = reverse("ticket_update", args=[self.ticket.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_other_cannot_edit(self):
        self.client.login(username="other", password="pass12345")
        url = reverse("ticket_update", args=[self.ticket.id])
        response = self.client.get(url)
        self.assertIn(response.status_code, [403, 302])

    def test_owner_can_delete(self):
        self.client.login(username="owner", password="pass12345")
        url = reverse("ticket_delete", args=[self.ticket.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_other_cannot_delete(self):
        self.client.login(username="other", password="pass12345")
        url = reverse("ticket_delete", args=[self.ticket.id])
        response = self.client.get(url)
        self.assertIn(response.status_code, [403, 302])