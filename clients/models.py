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
