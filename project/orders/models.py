from django.contrib.auth.models import User
from django.db import models


class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"id={self.pk!r} amount={self.amount!r} description={self.description!r}"
