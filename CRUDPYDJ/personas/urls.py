from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('registrar_vehiculo/',views.registrar_vehiculo,name='registrar_vehiculo'),
    path('listar_personas/',views.listar_personas,name='listar_personas'),
    path('pre_editar_persona/<str:id>/',views.pre_editar_persona,name='pre_editar_persona'),
    path('actualizar_persona/<str:id>/',views.actualizar_persona,name='actualizar_persona'),
    path('listar_vehiculos/',views.listar_vehiculos,name='listar_vehiculos'),
    
]
