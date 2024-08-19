from django.db import models


# Create your models here.
class CrearEvento(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Id Evento")
    nombre = models.TextField(verbose_name="Nombre del Evento")
    fecha = models.DateField(verbose_name="Fecha del Evento")
    hora = models.TimeField(verbose_name="Hora del Evento")
    lugar = models.TextField(verbose_name="Lugar del Evento")
    tipo = models.TextField(verbose_name="Tipo de Evento")
    descripcion = models.TextField(verbose_name="Descripcion del Evento")
    image = models.ImageField(upload_to='evento_imagenes', blank=True, null=True)
    class Meta:
        verbose_name = "Crear Evento"
        verbose_name_plural = "Crear Eventos"
        ordering = ["fecha"]
    def __str__(self):
        return self.nombre
    
class Eventos(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    evento= models.TextField(default='Eventos')
    precio = models.PositiveIntegerField(default=0)
    descripcion = models.TextField(default='Descripcion') #Texto largo
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado") #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Actualizado")
    
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ["-created"]
   
        #el menos indica que se ordenara del más reciente al más viejo

    def __str__(self):
        return self.evento
    