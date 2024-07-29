from urllib import request
from django.shortcuts import render
from .models import Alumnos
from .models import ComentarioContacto
from .forms import ComentarioContactoForm
from django.shortcuts import get_object_or_404


# Create your views here.
def registros(request):
    alumnos=Alumnos.objects.all()
    #all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request,"registros/principal.html",{'alumnos':alumnos})
    #Indicamos el lugar donde se renderizará el resultado de esta vista
    # y enviamos la lista de alumnos recuparados

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            comentariocontacto=ComentarioContacto.objects.all()
            return render(request,'registros/comentarios.html',{'comentariocontacto':comentariocontacto})
    form = ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/contacto.html',{'form': form})

def Contacto(request):
    return render(request,'registros/contacto.html')

def Comentarios(request):
    comentariocontacto=ComentarioContacto.objects.all()
    return render(request,'registros/comentarios.html',{'comentariocontacto':comentariocontacto})

def eliminarComentarioContacto(request, id,
    confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/comentarios.html",{'comentarios':comentarios})

    return render(request, confirmacion, {'object':comentario})

def consultarComentarioIndividual(request, id,):
    comentarios = ComentarioContacto.objects.get(id=id)
    return render(request,"registros/editar.html",{'comentarios':comentarios})

def editarComentarioContacto(request, id,):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    if form.is_valid():
        form.save()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/comentarios.html",{'comentarios':comentarios})
    return render(request, "registros/editar.html", {'comentario':comentario})





