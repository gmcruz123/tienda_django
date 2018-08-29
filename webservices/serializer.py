from rest_framework import serializers
from CLASS.models import Producto,Marca,Categoria

class producto_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('url','id','nombre','precio','status','marcas','foto','categoria')
        # fields = __all__


class marca_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca
        fields = ('url','id','nombre')
        # fields = __all__
        
class categoria_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('url','id','nombre')
        # fields = __all__
        