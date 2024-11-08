from django.shortcuts import render

from .models import SalesOrder


def orders_page(request):
    return render(request, "orders.html", {"orders": SalesOrder.objects.all()})
