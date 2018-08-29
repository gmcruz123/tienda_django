from django.shortcuts import render ,redirect
from .forms import *
from .models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def contacto(request):
    email = ""
    subject = ""
    text = ""
    info_enviado = False
    if request.method  == 'POST':
        formulario = Contacto_form(request.POST)
        if formulario.is_valid():
            email = formulario.cleaned_data['correo']
            subject = formulario.cleaned_data['asunto']
            text = formulario.cleaned_data['texto']
            info_enviado = True
            return render(request, 'contacto.html', locals())
        else:
            msg = 'La informacion no es correcta'
    else:
        formulario = Contacto_form()
    return render(request, 'contacto.html', locals())
    

def lista_productos_view (request):
    lista = Producto.objects.filter(status=True)
    return render(request, 'lista_productos.html',locals())

def agregar_producto_view (request):
    if request.method == 'POST':
        formulario = agregar_producto_form(request.POST, request.FILES)
        if formulario.is_valid():
                formulario.save() #guarda directament sobre la base de datos
                return redirect('/lista_productos/')
        else :
                msj = "Hay datos no validos"
    formulario = agregar_producto_form()
    return render(request,'agregar_producto.html',locals())

def ver_producto_view(request,id_prod):# el parametro debe llamarse igual que en la url (id_prod)
   
    try:
        obj = Producto.objects.get(id = id_prod)
    except:
        print("Error en la consulta, el producto no existe")
        msj = "El producto consultado no existe"
    return render(request,'ver_producto.html',locals())

def editar_producto_view(request,id_prod):
    obj= Producto.objects.get(id=id_prod)
    if request.method == 'POST':
        formulario = agregar_producto_form(request.POST,request.FILES,instance)
        if formulario.is_valid():
            #formulario.save(commit = false) #guarda la informacion en base de datos y en ram, si commit = false, guarda en memoria ram por defecto es true
             formulario.save()
            #formulario.save_m2m() antes se guardaban las relaciones many two many   
             return redirect('/lista_productos/')
    formulario = agregar_producto_form(instance=obj)
    return render (request,'agregar_producto.html',locals())

def eliminar_producto_view(request, id_prod):
    obj= Producto.objects.get(id=id_prod)
    obj.delete()
    return redirect('/lista_productos/')

def inactivar_producto_view(request,id_prod):
    obj = Producto.objects.get(id= id_prod)
    obj.status= False
    obj.save()
    return render('/lista_productos/')
    #Es recomendable manejar estados, no eliminar por ende se manejan los estados, de desactivar productos
    #por ejemplo en una tarjeta de credito no funciono pero se pregunta el porque igual queda el registro

