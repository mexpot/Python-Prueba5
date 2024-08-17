from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Alumnos(models.Model): #define la estructura de nuestra tabla
      matricula = models.CharField(max_length=12, verbose_name="Mat") #texto corto
      nombre = models.TextField(verbose_name="Nombre")
      carrera = models.TextField(default='carrera')
      turno = models.TextField(max_length=10, default='Turno')
      imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
      created = models.DateTimeField(auto_now_add=True, verbose_name="crear") #Fecha y tiempo 
      updated = models.DateTimeField(auto_now_add=True, verbose_name="actualizar")



      class Meta:
            verbose_name ="Alumno"
            verbose_name_plural ="Alumnos"
            ordering = ["-created"]
      #el menos indicado que se ordenara del mas reciente al mas viejo

      def __str__(self):
          return self.nombre
      
    #indicamos que se mostrara el nombre

class Comentario(models.Model):
      id = models.AutoField(primary_key=True,verbose_name="Clave")
      alumno = models.ForeignKey(Alumnos,
            on_delete=models.CASCADE,verbose_name="Alumno")
      created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
      coment = RichTextField(verbose_name="Comentario")
      
      
      class Meta:
            verbose_name = "Comentario"
            verbose_name_plural = "Comentarios"
            ordering = ["-created"]

      def __str__(self):
            return self.coment
      
class ComentarioContacto(models.Model):
      id = models.AutoField(primary_key=True,verbose_name="Clave")
      usuario = models.TextField(verbose_name="Usuario")
      mensaje = models.TextField(verbose_name="Comentario")
      created =models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
      class Meta:
            verbose_name = "Comentario Contacto"
            verbose_name_plural = "Comentarios Contactos"
            ordering = ["-created"]
      def __str__(self):
            return self.mensaje
      #Indica que se mostrára el mensaje como valor en la tabla