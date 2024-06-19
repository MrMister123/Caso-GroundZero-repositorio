from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('listadoSQL', views.listadoSQL, name='listadoSQL'),

    path('Menu', views.Menu, name='Menu'),
    path('VistaArtistas', views.VistaArtistas, name='VistaArtistas'),
    path('REGISTER', views.Register, name='REGISTER'),
    path('VistaMercado', views.VistaMercado, name='VistaMercado'),
    path('artes', views.Artes, name='artes'), 
    path('VistaCarrusel', views.VistaCarrusel, name='VistaCarrusel'),
    path('LOGIN', views.Login, name='LOGIN'),
    path('ARTICULO', views.Articulo, name='ARTICULO'),
    path('CARRITO', views.Carrito, name='CARRITO'),

    path('crud', views.crud, name='crud'),
    path('usuariosAdd', views.usuariosAdd, name='usuariosAdd'),
    path('usuarios_del/<str:pk>', views.usuarios_del, name='usuarios_del'),
    path('usuarios_findEdit/<str:pk>', views.usuarios_findEdit, name='usuarios_findEdit'),
    path('usuariosUpdate', views.usuariosUpdate, name='usuariosUpdate'),

    path('crud_generos', views.crud_generos, name='crud_generos'),
    path('generosAdd', views.generosAdd, name='generosAdd'),
    path('generos_del/<str:pk>', views.generos_del, name='generos_del'),
    path('generos_edit/<str:pk>', views.generos_edit, name='generos_edit'),

]
