from django.db import models


class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"id={self.pk!r} amount={self.amount!r} description={self.description!r}"
