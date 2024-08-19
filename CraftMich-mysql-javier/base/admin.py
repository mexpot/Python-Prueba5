from django.contrib import admin
from .models import Articulos

from .models import Contactos



# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id','producto', 'precio', 'descripcion')
    search_fields =('id', 'producto', 'precio')
    date_hierarchy = 'created'
    list_filter =('id', 'producto', 'precio',)
   
admin.site.register(Articulos, AdministrarModelo)
admin.site.register(Contactos)





