from rest_framework.decorators import api_view
from .models import Item,Title,SubItem
from .serializers import ItemSerializer,TitleSerializer,SubItemSerializer
from rest_framework.response import Response

# Create your views here.
#  GET views
@api_view(['GET'])
def get_titles(request):
    titles = Title.objects.all()
    serializer = TitleSerializer(titles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_subItems(request):
    subItems = SubItem.objects.all()
    serializer = SubItemSerializer(subItems, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_title(request,id):
    title = Title.objects.get(id=id)
    serializer = TitleSerializer(title, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def get_item(request,id):
    item = Item.objects.get(id=id)
    serializer = TitleSerializer(item, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def get_subItem(request,id):
    subItem = SubItem.objects.get(id=id)
    serializer = TitleSerializer(subItem, many=False)
    return Response(serializer.data)




# PUT views
@api_view(['PUT'])
def update_title(request,id):
    data = request.data
    title = Title.objects.get(id=id)
    serializer = TitleSerializer(instance=title, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update_item(request,id):
    data = request.data
    item = Item.objects.get(id=id)
    serializer = TitleSerializer(instance=item, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update_subItem(request,id):
    data = request.data
    subItem = SubItem.objects.get(id=id)
    serializer = TitleSerializer(instance=subItem, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# DELETE views
@api_view(["DELETE"])
def delete_title(request,id):
    title = Title.objects.get(id=id)
    title.delete()
    return Response("title was deleted")

@api_view(["DELETE"])
def delete_item(request,id):
    item = Item.objects.get(id=id)
    item.delete()
    return Response("item was deleted")

@api_view(["DELETE"])
def delete_subItem(request,id):
    subItem = SubItem.objects.get(id=id)
    subItem.delete()
    return Response("sub-item was deleted")

# POST views 

@api_view(["POST"])
def create_title(request):
    data = request.data
    serializer = TitleSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def create_item(request):
    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            print("serializer is valid")
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)
        
@api_view(['POST'])
def create_subItem(request):
    if request.method == 'POST':
        serializer = SubItemSerializer(data=request.data)
        if serializer.is_valid():
            print("serializer is valid")
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)
        




    