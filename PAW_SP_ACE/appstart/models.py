from django.db import models
from jsonfield import JSONField
from django import forms

class Usuario(models.Model):    
    rol = models.CharField('Rol', max_length=45,blank = False)
    correo = models.EmailField('Correo', max_length=45,blank=False)
    contrasena=models.CharField('Contraseña',max_length=45, null = True)
    paterno = models.CharField('Paterno', max_length=45,blank=False)
    materno = models.CharField('Materno', max_length=45,blank=False)
    nombre = models.CharField('Nombre', max_length=45,blank=False)
    nacimiento =  models.DateField()
    telefono = models.CharField('Teléfono',max_length=45) #NULL   
    domicilio = models.CharField('Domicilio', max_length=150) #NULL
    
    class ReadonlyMeta:
        readonly = ["contrasena"]
    #def __str__(self):
     #   return "%s User" % self.nombre

    
class Alumno(models.Model):   
    usuario = models.OneToOneField(Usuario,on_delete=models.CASCADE, primary_key=True,) #One to one relations
    #usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, null= True) 
    boleta = models.CharField('Boleta', max_length=10,blank = False)
    curp = models.CharField('CURP',max_length=18, blank = False)
    fecha_ingreso = models.DateField() #NULL

    def __str__(self):
        return "%s boleta" % self.boleta

    def display_usuario(self):
        """
        Creates a string for the Usuario. This is required to display genre in Admin.
        """
        return ', '.join([ usuario.nombre for usuario in self.usuario.all()[:3] ])  #Usariamos esto si la relacion es con muchos, en este caso es de uno la relacion

    display_usuario.short_description = 'Nombre'

class AlumnoInstance(models.Model):
    """
    Modelo que representa una copia específica de un libro (i.e. que puede ser prestado por la biblioteca).
    """
    usuario = models.OneToOneField(Alumno, on_delete=models.CASCADE, primary_key=True,) #One to one relations
    boleta = models.CharField('Boleta', max_length=10,blank = False)
    curp = models.CharField('CURP',max_length=18, blank = False)
    fecha_ingreso = models.DateField() #NULL      

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return "%s boleta" % self.boleta

class Agente(models.Model):   
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True,) #One to one relations
    folio = models.CharField('Folio', max_length=25,blank = False)
 
class Materia(models.Model):
    nivel = models.IntegerField('Nivel', null = False)
    nombre = models.CharField('Nombre', max_length=45, blank=False)
    carga = models.FloatField('Carga', null = False)

class ETS(models.Model):    
    turno = models.BooleanField()
    precio = models.FloatField('Precio', null = False)
    materia =  models.ForeignKey(Materia, related_name='etss', on_delete = models.CASCADE) #Many to one 
    #alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE) #Many to one
    fecha= models.DateField() 
    estatus = models.CharField('Estatus',max_length=25, blank = False)  

class Alumno_ETS(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE) #Many to one
    ets = models.ForeignKey(ETS, related_name='etss', on_delete = models.CASCADE) #Many to one
    #fecha= models.DateField() 
    #estatus = models.CharField('Estatus',max_length=25, blank = False)  


class Tipo_tramite(models.Model):
    nombre = models.CharField('Tipo de tramite', max_length=45, blank=False)

class Tramite(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE) #Many to one
    tipo_tramite = models.ForeignKey(Tipo_tramite, related_name='tipo_tramites', on_delete = models.CASCADE) #Many to one
    fecha_solicitud = models.DateField()
    ciclo_escolar = models.CharField('Ciclo escolar', max_length=6, blank=False)
    estatus = models.CharField('Estatus',max_length=25, blank= False)
    documento_firmado = models.FileField() #models.BinaryField()  
    comentario = models.TextField('Comentario',blank=False)
    atributos_dictamen = JSONField()
    qr = models.CharField('qr', max_length=128)
    firma = models.CharField('firma', max_length=128)

class Tipo_archivo(models.Model):
    nombre = models.CharField('Nombre', max_length=45, blank = False)

class Archivo_adjunto(models.Model):
    tramite = models.ForeignKey(Tramite, related_name='tramites', on_delete = models.CASCADE) #Many to one
    tipo_archivo = models.ForeignKey(Tipo_archivo, related_name='tipo_archivos', on_delete = models.CASCADE) #Many to one
    documento = models.FileField()

