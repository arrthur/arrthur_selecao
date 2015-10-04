from rest_framework import generics
from categoria.models.categoria_serializer import CategoriaSerializer
from categoria.models.categoria import Categoria


class Categoria_listar_serializer(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
        
