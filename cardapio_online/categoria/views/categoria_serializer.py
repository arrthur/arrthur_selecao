from rest_framework import generics
from categoria.models.categoria_serializer import CategoriaSerializer
from categoria.models.categoria import Categoria

class CategoriaSerial(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer