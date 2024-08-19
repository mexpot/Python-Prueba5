from django.db import models

# Create your models here.

class Articulos(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    categoria = models.TextField(default='artesania')
    producto = models.TextField(default='producto')
    ubicacion = models.TextField(default='ubicacion')
    precio = models.PositiveIntegerField(default=0)
    descripcion = models.TextField(default='Descripcion') #Texto largo
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado") #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Actualizado")
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-created"]
        #el menos indica que se ordenara del más reciente al más viejo
    
    def __str__(self):

        return self.producto
        #Indica que se mostrára el nombre como valor en la tabla

from django.db import models

class Login(models.Model):
    # Campos de texto
    usuario = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=25)
    fecha = models.DateTimeField()
    OPCIONES_ROL = [
        ('usuario', 'Usuario normal'),
        ('admin', 'Administrador'),
    ]
    roles = models.CharField(max_length=7, choices=OPCIONES_ROL, default='usuario')

class Contactos(models.Model):
    nombre=models.CharField(max_length=50)
    correo= models.EmailField()
    opciones_consulta=[
      [0, 'consulta'], 
      [1, 'Reclamo producto'],
      [2, 'Reclamo Eventos'],
      [3, 'Sugerencias de Eventos'],
      [4, 'Sugerencia de Productos']
    ]
    mensaje= models.TextField(default='mensaje')
    avisos= models.BooleanField()
    
    def __str__(self):
         return self.nombre

