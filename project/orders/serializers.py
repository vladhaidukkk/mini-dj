from products.serializers import ProductSerializer
from rest_framework import serializers

from .models import SalesOrder


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = SalesOrder
        fields = ["amount", "description", "products"]
