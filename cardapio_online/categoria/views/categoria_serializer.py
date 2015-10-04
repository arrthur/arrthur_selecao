from rest_framework import generics
from categoria.models.categoria_serializer import CategoriaSerializer
from ingrediente.models.ingrediente import Ingrediente

class CategoriaSerial(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingrediente.objects.all()
    serializer_class = CategoriaSerializer