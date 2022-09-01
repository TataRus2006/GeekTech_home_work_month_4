from django.contrib import admin

from .models import Client, Order


admin.site.register(Client)


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ["name", "contacts", "created_at", "finished"]           # отображение списка
    list_editable = ["contacts", "finished"]                                # редактируемый список
    fields = ["name", "client", "contacts", "description", "finished"]       # поля при добавлении
    readonly_fields = ["created_at", "updated_at"]                          # поля, доступные для чтения


admin.site.register(Order, OrderAdmin)
