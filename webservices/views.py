from django.shortcuts import render
from CLASS.models import Producto,Marca,Categoria
from .serializer import *
from rest_framework import viewsets




class producto_viewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = producto_serializer

class marca_viewset(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = marca_serializer

class categoria_viewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = categoria_serializer

# Create your views here.
