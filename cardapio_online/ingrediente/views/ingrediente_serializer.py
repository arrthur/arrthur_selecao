from rest_framework import generics
from categoria.models.categoria_serializer import CategoriaSerializer
from categoria.models.categoria import Categoria
from ingrediente.models.ingrediente_serializer import IngredienteSerializer

class IngredienteSerial(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = IngredienteSerializer