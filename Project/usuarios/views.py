from django.shortcuts import render

from .models import Usuario,Genero
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
