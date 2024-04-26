from django.urls import path
from .views import CargarInfraccionView, BearerTokenView

urlpatterns = [
    path('cargar_infraccion/',
         CargarInfraccionView.as_view(),
         name='cargar_infraccion'),
    path('obtener_token/', BearerTokenView.as_view(), name='obtener_token'),
]
