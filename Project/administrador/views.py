from django.shortcuts import render
from usuarios.models import Usuario
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def menuCrud(request):
    request.session["usuario"] = "dserey"
    usuario = request.session["usuario"]
    context = {'usuario':usuario}
    return render(request, 'administrador/crudMenu.html', context)

def home(request):
    context = {}
    return render(request, 'administrador/home.html', context)