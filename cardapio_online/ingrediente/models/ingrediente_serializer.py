from rest_framework import serializers
from ingrediente import Ingrediente


class IngredienteSerializer(serializers.ModelSerializer):
    
    
    
    class Meta:
        model = Ingrediente
        fields = ('id', 'nome')
        