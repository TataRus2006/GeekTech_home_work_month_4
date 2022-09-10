from email.policy import default
from django.contrib.auth.models import User
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

    description = models.TextField(null=True, blank=True, help_text="Вы можете добавить описание")
    name = models.CharField(max_length=255, help_text="Введите Ваше имя")
    contacts = models.CharField(max_length=255, help_text="Введите Ваш номер телефона, адрес электронной почты или "
                                                          "социальной сети")
    finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.contacts}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
