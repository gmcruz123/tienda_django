from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    # path('nosotros', views.nosotros),
    path('contacto/', views.contacto, name='contacto'),
    path('lista_productos/',views.lista_productos_view,name='listaProductos'),
    path('agregar_producto/',views.agregar_producto_view, name='agregar_producto'),
    path('ver_producto/<int:id_prod>', views.ver_producto_view, name='ver_producto'),
    path('editar_producto/<int:id_prod>', views.editar_producto_view, name='editar_producto'),
    path('eliminar_producto/<int:id_prod>', views.eliminar_producto_view, name='eliminar_producto'),
    #path('login/', views.login_view, name='login')
    
    #path('ver_producto/<str:nombre_prod>', ver_producto_view, name='ver_producto')
]