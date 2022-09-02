from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Client, Order


class ClientListView(ListView):
    model = Client
    template_name = 'clients.html'


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'


class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_create.html'
    fields = ["name", "contacts", "description"]
    success_url = "/orders/"


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_update.html'
    fields = ["name", "contacts", "description"]
    success_url = "/orders/"


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_delete.html'
    fields = ["name", "contacts", "description"]
    success_url = "/orders/"


class OrderInfoView(DetailView):
    model = Order
    template_name = "order_info.html"
