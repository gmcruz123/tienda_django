from django.urls import path, include
from rest_framework import routers
from webservices.views import *

router = routers.DefaultRouter()
router.register('productos',producto_viewset)
router.register('marca',marca_viewset)
router.register('categoria',categoria_viewset)

urlpatterns = [
    path('api/',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] 