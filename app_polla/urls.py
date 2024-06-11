from django.urls import path
from . import views

urlpatterns = [
    path('posiciones',views.posiciones, name='posiciones'), 
    path('',views.login_view, name='login'),    
    path('login',views.login_view, name='login'),    
    path('marcadores',views.marcadores, name='marcadores'),
    path('marcadores_usuario/<int:pk>',views.marcadores_usuario, name='marcadores_usuario'),
    path('marcadores_partido/<int:pk>',views.marcadores_partido, name='marcadores_partido'),
    path('cuadro_honor',views.cuadro_honor, name='cuadro_honor'),
    path('posiciones_playoff',views.posiciones_playoff, name='posiciones_playoff'),
    path('mis_marcadores',views.mis_marcadores, name='mis_marcadores'),
    path('marcador/new/<int:nro_partido>',views.marcador_new, name='marcador_new'),
    path('marcador/edit/<int:pk>',views.marcador_edit, name='marcador_edit'),
]