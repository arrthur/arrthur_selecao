from item.models.item import Item
from rest_framework import generics
from item.models.item_serializer import ItemSerializer, ItemSerializerList

class ItemSerial(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializerList