import uuid
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Summary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='summaries')

    total_income = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_expense = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} Summary"