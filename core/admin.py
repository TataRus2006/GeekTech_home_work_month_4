from django.contrib import admin
# core/admin.py
from .models import Bottle, BottlesCount


admin.site.register(Bottle)


class BottlesCountAdmin(admin.ModelAdmin):
    model = BottlesCount
    list_display = ["order", "bottle", "count"]
    list_editable = ["bottle", "count"]
    fields = ["order", "bottle", "count"]


admin.site.register(BottlesCount, BottlesCountAdmin)
