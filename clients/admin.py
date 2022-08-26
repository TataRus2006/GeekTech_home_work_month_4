from django.contrib import admin

from .models import Client, Order, BottlesCount


admin.site.register(Client)


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ["name", "contacts", "created_at", "finished"]
    list_editable = ["contacts", "finished"]
    fields = ["name", "contacts", "created_at", "updated_at", "description", "finished"]
    readonly_fields = ["created_at", "updated_at"]


admin.site.register(Order, OrderAdmin)


class BottlesCountAdmin(admin.ModelAdmin):
    model = BottlesCount
    list_display = ["order", "bottle", "count", "finished"]
    list_editable = ["bottle", "count", "finished"]
    fields = ["order", "bottle", "count", "finished"]


admin.site.register(BottlesCount, BottlesCountAdmin)
