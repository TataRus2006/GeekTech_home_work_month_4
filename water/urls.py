from django.contrib import admin
from django.urls import path
from clients.views import clients_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', clients_list)
]
