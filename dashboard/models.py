from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    STATUS = (
        ("Open", "Open"),
        ("Closed", "Closed")
    )
    user = models.ForeignKey(User, default=1)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=3000)
    status = models.CharField(max_length=10, choices=STATUS, default='Open')
    # User
    author = User.username
    # User
    assignee = models.CharField(max_length=100)
    # Date
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.title + " - " + self.body
