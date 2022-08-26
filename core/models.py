from django.db import models
from clients.models import Order


class Bottle(models.Model):
    volume = models.IntegerField(default=10, null=True, blank=True)
    maker = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    expired = models.BooleanField(default=False, null=True, blank=True)


class BottlesCount(models.Model):
    bottle = models.ForeignKey(to=Bottle, on_delete=models.SET_NULL, null=True, blank=True, related_name="bottle_count")
    count = models.IntegerField(default=1)
    order = models.ForeignKey(to=Order, on_delete=models.SET_NULL, null=True, blank=True, related_name="bottle_count")

    def __str__(self):
        return f"{self.bottle} - {self.count} - {self.order}"
