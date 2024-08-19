from django.shortcuts import render, HttpResponse
from .forms import CrearEventoForm,EventosForm
from .models import CrearEvento,Eventos
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required



# Create your views here.
def ca(request):
    return render(request, "michoacan/ca.html")

def bienvenida(request):
    return render(request, "michoacan/bienvenida.html")

def Quienessomos(request):
    return render(request, "michoacan/Quienessomos.html")

#@login_required
def CrearEventos(request):
    if request.method == 'POST':
        form = CrearEventoForm(request.POST, request.FILES)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            evento=CrearEvento.objects.all()
            return render(request,"michoacan/consultarEventos.html",
                {'evento':evento})

    form = CrearEventoForm()
#Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'michoacan/crearEvento.html',{'form': form})

#@login_required
def ConsultarEvento(request):
    evento=CrearEvento.objects.all()
    return render(request,"michoacan/consultarEventos.html",
        {'evento':evento})


def eliminarEvento(request, id,
    confirmacion ='michoacan/confirmarEliminacion.html'):
    evento = get_object_or_404(CrearEvento, id=id)
    if request.method=="POST":
        evento.delete()
        eventos=CrearEvento.objects.all()
        return render(request,"michoacan/consultarEventos.html",
        {'eventos':eventos})

    return render(request, confirmacion, {'object':evento})

def ConsultarEventoIndividual(request, id):
    evento = CrearEvento.objects.get(id=id)
    return render(request,"michoacan/editarEventos.html",
    {'evento':evento})


def editarEvento(request, id):
    evento = get_object_or_404(CrearEvento, id=id)
    form = CrearEventoForm(request.POST, instance=evento)
    if form.is_valid():
        form.save() #si el registro ya existe, se modifica.
        eventos=CrearEvento.objects.all()
        return render(request,"michoacan/consultarEventos.html",
        {'eventos':eventos})
    return render(request,"michoacan/editarEventos.html",
    {'evento':evento})

def eventos(request):
    eventos= CrearEvento.objects.all()
    return render(request,"michoacan/eventos.html", {'eventos':eventos})

