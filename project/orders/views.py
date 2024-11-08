from django.shortcuts import render
from rest_framework import viewsets

from .models import SalesOrder
from .serializers import OrderSerializer


def orders_page(request):
    return render(request, "orders.html", {"orders": SalesOrder.objects.all()})


class OrderViewSet(viewsets.ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerializer
