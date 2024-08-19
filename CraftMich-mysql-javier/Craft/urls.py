"""
URL configuration for Craft project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from michoacan import views
from django.conf import settings
from base import views as views_base
from django.conf.urls.static import static
from michoacan import views as views_mich

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ca/', views.ca, name="ca"),
    path('producto/',views_base.producto,name="Producto"),
    path('eliminarCarrusel/<int:id>/',views_base.eliminarCarrusel, name='Eliminarcarrusel'),
    path('editarCarrusel/<int:id>/',views_base.editarCarrusel, name='Editarcarrusel'),
    path('mascarrusel/<int:id>/', views_base.mascarrusel, name='Mascarrusel'),
    path('carrusel2', views_base.carrusel2, name="carrusel2"),
    path('carrusel3', views_base.carrusel3, name="carrusel3"),
    path('carrusel4', views_base.carrusel4, name="carrusel4"),

    
    path('bienvenida/', views.bienvenida, name="bienvenida"),
    path('Quienessomos/', views.Quienessomos, name="Quienessomos"),
    path('registro/', views_base.registro, name="Registro"),
    path('login/', views_base.login, name="Login"),
    path('', views_base.Carrusel, name="Carrusel"),
    path('accounts', include('django.contrib.auth.urls')),
    path('CrearEvento/', views_mich.CrearEventos, name="CrearEvento"),
    path('ConsultarEvento/', views_mich.ConsultarEvento, name="ConsultarEvento"),
    path('eliminarEvento/<int:id>/',views_mich.eliminarEvento,name='Eliminar'),
    path('formEditarEvento/<int:id>/',views_mich.ConsultarEventoIndividual, name='ConsultaIndividual'),
    path('editarEvento/<int:id>/',views_mich.editarEvento,name='Editar'),
    path('Contactos/',views_base.Contactos,name="Contactos"),
     path('eventos', views_mich.eventos, name="eventos"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)