from django.shortcuts import render, HttpResponse, redirect
# core/views.py
from .models import Bottle
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.models import AnonymousUser


def contacts(request):
    return render(request, 'core/contacts.html')


def about(request):
    return render(request, 'about.html')


def makers_list(request):
    context = {}
    # SELECT * FROM Bottle
    bottles_list = Bottle.objects.all()
    context["bottles_list"] = bottles_list
    html_page = render(request, 'makers.html', context)
    return html_page


def products_list(request):
    return render(request, 'products.html')


class LoginView(View):
    def get(self, request):
        context = {"form": LoginForm()}
        return render(request, 'auth/sign_in.html', context)

    def post(self, request, *args, **kwargs):
        data = request.POST
        user_login = data["username"]
        password = data["password"]
        user = authenticate(request, username=user_login, password=password)
        if user is not None:
            login(request, user)
            return redirect(products_list)
        else:
            return HttpResponse("Не верный логин или пароль")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(products_list)

