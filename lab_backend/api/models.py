from django.db import models

# Create your models here.

class Item(models.Model):
    item = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.item