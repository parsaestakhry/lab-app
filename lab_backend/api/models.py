from django.db import models

# Create your models here.

class Item(models.Model):
    item = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.item

class SubItem (models.Model):
    sub_item = models.CharField(max_length=128)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.sub_item
    
