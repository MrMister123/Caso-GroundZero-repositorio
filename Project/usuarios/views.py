from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Usuario, Genero

from .forms import GeneroForm
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

def crud(request):
    usuarios = Usuario.objects.all()
    context = {'usuarios': usuarios}
    return render(request, 'usuarios/usuarios_list.html', context)

def usuariosAdd(request):
    if request.method is not "POST":
        generos=Genero.objects.all()
        context={'generos':generos}
        return render(request, 'usuarios/usuarios_add.html', context)
    else:
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"

        objGenero=Genero.objects.get(id_genero = genero)
        obj=Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            apellido_paterno=aPaterno,
            apellido_materno=aMaterno,
            fecha_nacimiento=fechaNac,
            id_genero=objGenero,
            telefono=telefono,
            email=email,
            direccion=direccion,
            activo=1
        )
    obj.save()
    context={'mensaje':"Ok, datos grabados..."}
    return render(request, 'usuarios/usuarios_add.html', context)

def usuarios_del(request,pk):
    context=()
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

def usuarios_findEdit(request, pk):
    if pk != "":
        usuario=Usuario.objects.get(rut=pk)
        generos=Genero.objects.all()
        print(type(usuario.id_genero.genero))

        context = {'usuario':usuario, 'generos':generos}
        if usuario:
            return render(request, 'usuarios/usuarios_edit.html', context)
        else:
            context = {'mensaje':"Error, rut no existe..."}
            return render(request, 'usuarios/usuarios_list.html', context)

def crud_generos(request):
    generos = Genero.objects.all()
    context = {'generos':generos}
    print("enviando datos generos_list")
    return render(request, "alumnos/generos_list.html", context)

def generosAdd(request):
    print("estoy en controlador generosAdd...")
    context = {}

    if request.method == "POST":
        print("controlador es un post...")
        form = GeneroForm(request.POST)
        if form.is_valid:
            print("estoy en agregar, is_valid")
            form.save()

            #limpiar form
            form = GeneroForm()

            context = {'mensaje':"Ok. datos grabados...","form":form}
            return render(request, "usuarios/generos_add.html", context)