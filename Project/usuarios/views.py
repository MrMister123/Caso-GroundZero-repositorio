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

def usuariosUpdate(request):
    if request.method == "POST":
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

        usuario = Usuario()
        usuario.rut=rut
        usuario.nombre=nombre
        usuario.apellido_paterno=aPaterno
        usuario.apellido_materno=aMaterno
        usuario.fecha_nacimiento=fechaNac
        usuario.id_genero=objGenero
        usuario.telefono=telefono
        usuario.email=email
        usuario.direccion=direccion
        usuario.activo=1
        usuario.save()

        generos = Genero.objects.all()
        context = {'mensaje': "Ok, datos actualizados...", 'generos': 
                   generos, 'usuario': usuario}
        return render(request, 'usuarios/usuarios_edit.html', context)
    else:
        usuarios = Usuario.objects.all()
        context = {'usuarios': usuarios}
        return render(request, 'usuarios/usuarios_list.html', context)

def crud_generos(request):
    generos = Genero.objects.all()
    context = {'generos':generos}
    print("enviando datos generos_list")
    return render(request, "usuarios/generos_list.html", context)

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
        else:
            form = GeneroForm()
            context={'form':form}
            return render(request, 'usuarios/generos_add.html', context)
        
def generos_del(request, pk):
    mensajes=[]
    errores=[]
    generos = Genero.object.all()
    try:
        genero=Genero.objects.all(id_genero=pk)
        context={}
        if genero:
            genero.delete()
            mensajes.append("Bien, datos eliminados...")
            context = {'generos': generos, 'mensajes': mensajes, 'errores':errores}
            return render(request, 'usuarios/generos_list.html', context)
    except:
        print("Error, id no existe...")
        generos=Genero.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje': mensaje,'generos': generos}
        return render(request, 'usuarios/generos_list.html', context)
    
def generos_edit(request, pk):
    try:
        genero=Genero.objects.get(id_genero=pk)
        context={}
        if genero:
            print("Edit encontró el género...")
            if request.method == "POST":
                print("Edit, es un POST")
                form = GeneroForm(request.POST, instance=genero)
                form.save()
                mensaje="Bien, datos actualizados..."
                print(mensaje)
                context = {'genero': genero, 'form': form, 'mensaje': mensaje}
                return render(request, 'usuarios/generos_edit.html', context)
            else:
                print("Edit, NO es un POST")
                form = GeneroForm(instance=genero)
                mensaje = "" 
                context = {'genero': genero, 'form': form, 'mensaje': mensaje}
                return render(request, 'usuarios/generos_edit.html', context)
    except:
        print("Error, id no existe...")
        generos = Genero.object.all
        mensaje = "Error, id no existe"
        context = {'mensaje': mensaje, 'generos': generos}
        return render(request, 'usuarios/generos_list', context)
    