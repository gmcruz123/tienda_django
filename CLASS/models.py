from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
#Django coloca el id automaticamente por ende n se define

    def __str__(self):
        return self.nombre



class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
#Django coloca el id automaticamente por ende n se define

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField(null=True,blank=True)
    status = models.BooleanField(default= True)
    # En la base de datos me permite el campo vacio el formulario tambien me lo permite vacio
    foto = models.ImageField(upload_to='fotos',null=True,blank=True)
    #Especificamos una caracteristica , django maneja un orm podemos eliminar en cascada, la idea es 
    #que si elimino una marca no me elimine todos los productos que estan bajo esa marca
    #se coloa on_cascada
    #Marca es llave foranea porque  muchos productos le corresponde una sola marca
    marcas = models.ForeignKey(Marca, on_delete=models.PROTECT)
    #Le paso null y blank porque un producto no necesariamente puede estar creada la acategoria
    categoria = models.ManyToManyField(Categoria,null=True,blank=True)

    def __str__(self):
        return self.nombre

    # Comando para chequear problemas python manage.py check
    # Crear migraciones python manage.py makemigrations
    # Migrar la base de datos python manage.py migrate
    # ejmp
    # Si se ejerce algun cambio en los modelos por ejemplo agragdno campos o destinando algunos a ser nulos entonces de nuevo se
    # deben hacer las migraciones python manage.py makemigrations