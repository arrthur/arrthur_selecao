from rest_framework import generics
from ingrediente.models.ingrediente_serializer import IngredienteSerializer
from ingrediente.models.ingrediente import Ingrediente


class Ingrediente_listar_serializer(generics.ListCreateAPIView):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    
        
