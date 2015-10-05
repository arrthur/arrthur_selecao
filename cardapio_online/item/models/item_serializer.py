from item import Item
from rest_framework import serializers


class ItemSerializerList(serializers.ModelSerializer):
    ingrediente = serializers.StringRelatedField(many=True)
    categoria = serializers.StringRelatedField()
    
    class Meta:
        model = Item
        fields = ('id', 'nome', 'valor', 'tempo_preparo', 'ingrediente', 'categoria')
        
class ItemSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Item
        fields = ('id', 'nome', 'valor', 'tempo_preparo', 'ingrediente', 'categoria')