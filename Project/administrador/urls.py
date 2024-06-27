from django.urls import path
from . import views

app_name = 'administrador'
urlpatterns = [
    path('crudMenu', views.menuCrud, name = 'crudMenu'),
    path('home', views.home, name = 'home'),
]