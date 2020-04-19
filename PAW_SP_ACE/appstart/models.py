from django.db import models

# Create your models here.

class Usuario(models.Model):    
    rol = models.CharField('Rol', max_length=45,blank = False)
    correo = models.CharField('Correo', max_length=45,blank=False)
    contrasena=models.CharField('Contraseña',max_length=30,blank=False)
    paterno = models.CharField('Paterno', max_length=45,blank=False)
    materno = models.CharField('Materno', max_length=45,blank=False)
    nombre = models.CharField('Nombre', max_length=45,blank=False)
    nacimiento =  models.DateField()
    telefono = models.IntegerField('Teléfono',null=True) #NULL   
    domicilio = models.CharField('Domicilio', max_length=150) #NULL

    def __str__(self):
        return "%s User" % self.nombre

class Alumno(models.Model):   
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True,) #One to one relations
    boleta = models.CharField('Boleta', max_length=10,blank = False)
    curp = models.CharField('CURP',max_length=18, blank = False)
    fecha_ingreso = models.DateField() #NULL

    def __str__(self):
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
    materia =  models.ForeignKey(Materia, related_name='materias', on_delete = models.CASCADE) #Many to one

class Alumno_ETS(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE) #Many to one
    ets = models.ForeignKey(ETS, related_name='etss', on_delete = models.CASCADE) #Many to one
    fecha= models.DateField() 
    estatus = models.CharField('Estatus',max_length=25, blank = False)  

class Tipo_tramite(models.Model):
    nombre = models.CharField('Tipo de tramite', max_length=45, blank=False)

class Tramite(models.Model):
    alumno = models.ForeignKey(Alumno, related_name='alumnos', on_delete = models.CASCADE) #Many to one
    tipo_tramite = models.ForeignKey(Tipo_tramite, related_name='tipo_tramites', on_delete = models.CASCADE) #Many to one
    fecha_solicitud = models.DateField()
    ciclo_escolar = models.CharField('Ciclo escolar', max_length=6, blank=False)
    estatus = models.CharField('Estatus',max_length=25, blank= False)
    documento = models.BinaryField()
    comentario = models.TextField('Comentario')

class Tipo_archivo(models.Model):
    nombre = models.CharField('Nombre', max_length=45, blank = False)

class Archivo_adjunto(models.Model):
    tramite = models.ForeignKey(Tramite, related_name='tramites', on_delete = models.CASCADE) #Many to one
    tipo_archivo = models.ForeignKey(Tipo_archivo, related_name='tipo_archivos', on_delete = models.CASCADE) #Many to one
    documento = models.BinaryField()


    