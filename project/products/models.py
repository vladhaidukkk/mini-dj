from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return f"id={self.pk!r} name={self.name!r} price={self.price!r} description={self.description!r}"
