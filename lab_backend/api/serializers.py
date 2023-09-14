from rest_framework import serializers
from .models import Item,SubItem,Title

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

class SubItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubItem
        fields = "__all__"

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = "__all__"