from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    bottles_ordered = models.IntegerField(default=1)
    photo = models.ImageField(
        verbose_name="фотография",
        upload_to='photo',
        null=True,
        blank=True
    )

class Order(models.Model):
    client = models.ForeignKey(
        to=Client, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="order"
    )

    created_at = models.DateTimeField(
        verbose_name="Дата и время создания заказа",
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name="Дата и время изменения заказа",
        auto_now=True,
    )

    description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.contacts}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class BottlesCount(models.Model):
    bottle = models.ForeignKey(to=Client, on_delete=models.SET_NULL, null=True, blank=True, related_name="bottle")
    count = models.IntegerField()
    order = models.ForeignKey(to=Order, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.bottle} {self.count} {self.order}"
