"""
URL configuration for prueba project.

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
from django.urls import path
from inicio import views 
from django.conf import settings
from registros import views as views_registros

#permite acceder a las variables MEDIA_URL y MEDIA_ROOT que
#almacenan la ubicación de nuestras imagenes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_registros.registros, name="Principal"), #Indicamos que ahora la ruta de principal.html se encuentra en la view de registros
    path('contacto/',views_registros.Contacto, name="Contacto"),
    path('formulario/',views.formulario, name="Formulario"),
    path('ejemplo/',views.ejemplo, name="ejemplo"),
    path('registrar/',views_registros.registrar, name="Registrar"),
    path('comentarios/',views_registros.Comentarios, name="Comentarios"),
    path('eliminarComentario/<int:id>/',views_registros.eliminarComentarioContacto, name='Eliminar'),
    path('editarComentarioContacto/<int:id>/',views_registros.editarComentarioContacto, name='Editar'),
    path('consultarComentarioIndividual/<int:id>/',views_registros.consultarComentarioIndividual, name='consultarComentarioIndividual'),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                document_root=settings.MEDIA_ROOT)