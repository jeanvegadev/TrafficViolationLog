from django.urls import path
from .views import (CargarInfraccionView, BearerTokenView,
                    GenerarInformeView)

urlpatterns = [
    path('cargar_infraccion/',
         CargarInfraccionView.as_view(),
         name='cargar_infraccion'),
    path('generar_informe/',
         GenerarInformeView.as_view(),
         name='generar_informe'),
    path('obtener_token/', BearerTokenView.as_view(), name='obtener_token'),
]
