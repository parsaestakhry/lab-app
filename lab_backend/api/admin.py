from django.contrib import admin
from .models import Item,SubItem,Title

# Register your models here.
admin.site.register(Item)
admin.site.register(SubItem)
admin.site.register(Title)
