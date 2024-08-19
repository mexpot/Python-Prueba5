from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .models import Articulos
from .form import LoginForm
from .forms import ArticulosForm,ContactosForm
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404

# Create your views here.
def Carrusel(request):
    articulos=Articulos.objects.all()
    return render(request,"base/Carrusel.html", {'articulos':articulos})

def producto(request):
    if request.method == 'POST':
        form = ArticulosForm(request.POST, request.FILES)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            return render(request,'base/ForCarrusel.html')
    form = ArticulosForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'base/ForCarrusel.html',{'form': form})

def eliminarCarrusel(request, id,
    confirmacion='base/eliminarproducto.html'):
    articulo = get_object_or_404(Articulos, id=id)
    if request.method=='POST':
        articulo.delete()
        articulos=Articulos.objects.all()
        return render(request,"base/Carrusel.html",{'articulos':articulos})

    return render(request, confirmacion, {'object':articulo})

def editarCarrusel(request, id):
    articulo = get_object_or_404(Articulos, id=id)
    form = ArticulosForm(request.POST, request.FILES, instance=articulo)
    if form.is_valid():
        form.save()
        articulos=Articulos.objects.all()
        return render(request,"base/Carrusel.html",{'articulos':articulos})
    return render(request, "base/editarproducto.html", {'articulo':articulo})

def mascarrusel(request, id):
    articulo_id = int(id)  # Asegúrate de que el id es un número entero
    articulo = get_object_or_404(Articulos, id=articulo_id)
    return render(request, "base/mascarrusel.html", {'articulo': articulo})

def carrusel2(request):
    articulosr=Articulos.objects.filter(categoria="ropa")
    return render(request,"base/carrusel2.html", {'articulosr':articulosr})

def carrusel3(request):
    articulosa=Articulos.objects.filter(categoria="accesorios")
    return render(request,"base/carrusel3.html", {'articulosa':articulosa})

def carrusel4(request):
    articulosd=Articulos.objects.filter(categoria="decoraciones")
    return render(request,"base/carrusel4.html", {'articulosd':articulosd})









def registro(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            # hacer algo después de guardar los datos del usuario
    else:
        form = LoginForm()
    return render(request, 'base/registro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('bienvenida')  
            HttpResponse('Ir a home')# Redirige a la página deseada después del login
                
    else:
        form = AuthenticationForm()
    return render(request, 'base/login.html', {'form': form})


class VRegistro(View):
    def post(self, request):
        form=UserCreationForm()
        return render(request, 'base/registro.html', {'form': form})
    

    def post(selft, request):
       form= UserCreationForm(request.POST)
       if form.is_valid():
            username =form.save()
            login(request,username)
            return redirect('home')
       else:
           pass
        





def Contactos(request):
    data={
        'form': ContactosForm()
    }
    if request.method == 'POST':
     
     formulario= ContactosForm(data=request.POST)
     if formulario.is_valid():
         formulario.save()
         data["mensaje"] = "Contacto guardado"
    


    return render(request,"base/contactanos.html", data)
