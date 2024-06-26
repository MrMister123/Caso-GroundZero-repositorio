from django.urls import path
from . import views

urlpatterns = [
    path('crudMenu', views.menuCrud, name = 'crudMenu'),
    path('home', views.home, name = 'home')

]