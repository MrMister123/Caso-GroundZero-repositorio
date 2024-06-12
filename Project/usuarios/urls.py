from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('listadoSQL', views.listadoSQL, name='listadoSQL'),
    path('Menu', views.Menu, name='Menu'),

    path('crud', views.crud, name='crud'),
    path('usuariosAdd', views.usuariosAdd, name='usuariosAdd'),
    path('usuarios_del/<str:pk>', views.usuarios_del, name='usuairos_del'),
    path('usuarios_findEdit/<str:pk>', views.usuarios_findEdit, name='usuarios_findEdit'),

    path('crud_generos', views.crud_generos, name='crud_generos'),

]
