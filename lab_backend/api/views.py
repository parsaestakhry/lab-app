from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def get_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)



