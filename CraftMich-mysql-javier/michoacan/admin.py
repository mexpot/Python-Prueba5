from django.contrib import admin
from .models import CrearEvento
from .models import Eventos


# Register your models here.
class administrarCrearEvento(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('id','nombre')
    date_hierarchy = 'fecha'
    readonly_fields = ('id', 'fecha')
admin.site.register(CrearEvento, administrarCrearEvento)

class administrarEventos(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id','evento', 'precio', 'descripcion')
    search_fields =('id', 'evento', 'precio')
    date_hierarchy = 'created'
    list_filter =('id', 'evento', 'precio',)
admin.site.register(Eventos, administrarEventos)



