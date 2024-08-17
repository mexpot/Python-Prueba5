from urllib import request
from django.conf.urls.static import static
from django.shortcuts import render
from .models import Alumnos
from .models import ComentarioContacto
from .forms import ComentarioContactoForm, AlumnosForm
from django.shortcuts import get_object_or_404
import datetime


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

def registrocursos(request):
    if request.method == 'POST':
        form = AlumnosForm(request.POST, request.FILES)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            return render(request,'registros/formulario.html')
    form = AlumnosForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/formulario.html',{'form': form})

def formulario(request):
   return render(request, "registros/formulario.html")


#Función FILTER
# filter nos retornará los registros que coinciden con los parámetros
#de búsqueda dados.

def consultar1(request):
    #con una sola condición
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})


def consultar2(request):
    #multiples condiciones adicionando .filter() se analiza #como AND
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar3(request):
    #Si solo deseamos recuperar ciertos datos agregamos la #función only,
   # listando los campos que queremos obtener de #la consulta emplear
    #filter() o #en el ejemplo all()
    alumnos=Alumnos.objects.all().only("matricula", "nombre", "carrera",
    "turno", "imagen")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["Juan", "Ana"])
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar6(request):
    fechaInicio = datetime.date(2024, 7, 20)
    fechaFin = datetime.date(2024, 8, 30)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar7(request):
    #Consultando entre modelos
    alumnos=Alumnos.objects.filter(comentario__coment__contains='No inscrito')
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultasSQL(request):

    alumnos=Alumnos.objects.raw('SELECT id, matricula,nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request,"registros/consultas.html",{'alumnos':alumnos})