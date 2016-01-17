from item.models.item_serializer import ItemSerializer, ItemSerializerList
from item.models.item import Item
from rest_framework import generics



class Lista_item_serializer(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializerList
    
    
class Criar_item_serializer(generics.CreateAPIView):
    serializer_class = ItemSerializer
    
        
