from django.shortcuts import render, HttpResponse
from .models import Client, Order
from .forms import OrderForm


def clients_list(request):
    context = {}
    order_data = Client.objects.all()
    context['order_data'] = order_data
    return render(request, 'clients.html', context)


def order_list(request):
    return render(request, 'order_list.html', {"order_list": Order.objects.all()})


def order_info(request, id):
    return render(
        request,
        'order_info.html',
        {'order_object': Order.objects.get(id=id)}
    )



def order_create(request):
    context = {}
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            return render(request, 'order_list.html', {"order_list": Order.objects.all()})
        return HttpResponse("Данные не валидны")

    context["order_form"] = OrderForm()
    return render(request, 'order_create.html', context)


def order_delete(request, id):
        context = {}
        if request.method == "POST":
            order_object = Order.objects.get(id=id)
            order_object.delete()
            return render(request, 'order_list.html', {"order_list": Order.objects.all()})
        context["form"] = OrderForm()
        return render(request, 'order_delete.html', context)


def order_update(request, id):
    context = {}
    order_object = Order.objects.get(id=id)
    if request.method == 'POST':
        order = OrderForm(request.POST, instance=order_object)
        if order.is_valid():
            order_object.save()
            return render(request, 'order_list.html', {"order_list": Order.objects.all()})

    context['order'] = OrderForm(instance=order_object)
    return render(request, 'order_update.html', context)
