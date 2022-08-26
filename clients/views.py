from django.shortcuts import render
from .models import Client


def clients_list(request):
    context = {}
    order_data = Client.objects.all()
    context['order_data'] = order_data
    return render(request, 'clients.html', context)

