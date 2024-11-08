from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    product_details = models.OneToOneField("ProductDetails", on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"id={self.pk!r} name={self.name!r} price={self.price!r} description={self.description!r}"


class ProductDetails(models.Model):
    rating = models.IntegerField()
    warranty = models.IntegerField()

    def __str__(self) -> str:
        return f"id={self.pk!r} rating={self.rating!r} warranty={self.warranty!r}"
