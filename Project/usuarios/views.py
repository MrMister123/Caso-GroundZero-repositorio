from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Usuario
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    usuarios=Usuario.objects.all()
    context={"usuarios":usuarios}
    return render(request, 'usuarios/index.html', context)

def listadoSQL(request):
    usuarios= Usuario.objects.raw('SELECT * FROM usuarios_usuario')
    print(usuarios)
    context={"usuarios":usuarios}
    return render(request, 'usuarios/listadoSQL.html', context)


def Menu(request):
    return render(request, 'usuarios/Menu.html')

def VistaArtistas(request):
    return render(request, 'usuarios/VistaArtistas.html')

def Register(request):
    return render(request, 'usuarios/REGISTER.html')

def VistaMercado(request):
    return render(request, 'usuarios/VistaMercado.html')

def Artes(request):
    return render(request, 'usuarios/artes.html')

def VistaCarrusel(request):
    return render(request, 'usuarios/VistaCarrusel.html')

def Login(request):
    return render(request, 'usuarios/LOGIN.html')

def Articulo(request):
    return render(request, 'usuarios/ARTICULO.html')

def Carrito(request):
    return render(request, 'usuarios/CARRITO.html')


@login_required
def crud(request):
    request.session["usuario"] = "dserey"
    usuarios = Usuario.objects.all()
    context = {'usuarios': usuarios}
    return render(request, 'usuarios/usuarios_list.html', context)

@login_required
def usuariosAdd(request):
    request.session["usuario"] = "dserey"
    if request.method != "POST":
        return render(request, 'usuarios/usuarios_add.html')
    else:
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        email=request.POST["email"]
        activo="1"

        obj=Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            email=email,
            activo=1
        )
    obj.save()
    context={'mensaje':"Ok, datos grabados..."}
    return render(request, 'usuarios/usuarios_add.html', context)

@login_required
def usuarios_del(request,pk):
    request.session["usuario"] = "dserey"
    context={}
    try:
        usuario = Usuario.objects.get(rut=pk)

        usuario.delete()
        mensaje = "Bien, datos eliminados..."
        usuarios = Usuario.objects.all()
        context = {'usuarios': usuarios, 'mensaje': mensaje}
        return render(request, 'usuarios/usuarios_list.html', context)
    except:
        mensaje = "Error, rut no existe..."
        usuarios = Usuario.objects.all()
        context = {'usuarios': usuarios, 'mensaje': mensaje}
        return render(request, 'usuarios/usuarios_list.html', context)

@login_required
def usuarios_findEdit(request, pk):
    request.session["usuario"] = "dserey"
    if pk != "":
        usuario=Usuario.objects.get(rut=pk)

        context = {'usuario':usuario}
        if usuario:
            return render(request, 'usuarios/usuarios_edit.html', context)
        else:
            context = {'mensaje':"Error, rut no existe..."}
            return render(request, 'usuarios/usuarios_list.html', context)

@login_required
def usuariosUpdate(request):
    request.session["usuario"] = "dserey"
    if request.method == "POST":
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        email=request.POST["email"]
        activo="1"
        usuario = Usuario()
        usuario.rut=rut
        usuario.nombre=nombre
        
        usuario.email=email
        usuario.activo=1
        usuario.save()
        context = {'mensaje': "Ok, datos actualizados...", 'usuario': usuario}
        return render(request, 'usuarios/usuarios_edit.html', context)
    else:
        usuarios = Usuario.objects.all()
        context = {'usuarios': usuarios}
        return render(request, 'usuarios/usuarios_list.html', context)