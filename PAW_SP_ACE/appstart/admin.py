from django.contrib import admin
from . import models

# Register your models here.
#admin.site.register(models.Usuario)
admin.site.register(models.Agente)
admin.site.register(models.Materia)
admin.site.register(models.ETS)

class AlumnoInstanceInline(admin.TabularInline):
    model = models.AlumnoInstance

####FORMA 1 DE DECLARAR SIN  DECORADORES

# Define the admin class
#class AlumnoAdmin(admin.ModelAdmin):
 #   list_display = ('usuario', 'boleta')
    #list_filter = ('fecha_ingreso')  ##must be a list or tuple.
  #  pass

# Register the admin class with the associated model
#admin.site.register(models.Alumno, AlumnoAdmin)


##FORMA 2 DE DECLARAR USANDO DECORADORES
# Register the Admin classes and register at the same time, using the decorator

@admin.register(models.Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'boleta')
    inlines = [AlumnoInstanceInline]
    pass

@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre','paterno','materno')
    pass

