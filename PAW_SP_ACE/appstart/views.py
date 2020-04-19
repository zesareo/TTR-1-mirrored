from django.shortcuts import render
from .models import Usuario,Alumno,Agente,Materia,ETS,Alumno_ETS,Tipo_tramite,Tramite,Tipo_archivo,Archivo_adjunto
from .serializers import UsuarioSerializer,AlumnoSerializer,AgenteSerializer,MateriaSerializer,ETSSerializer,Alumno_ETSSerializer,Tipo_tramiteSerializer,TramiteSerializer,Tipo_archivoSerializer,Archivo_adjuntoSerializer
from rest_framework import generics

# Create your views here.
class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class AlumnoListCreate(generics.ListCreateAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class AgenteListCreate(generics.ListCreateAPIView):
    queryset = Agente.objects.all()
    serializer_class = AgenteSerializer

class MateriaListCreate(generics.ListCreateAPIView):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

class ETSListCreate(generics.ListCreateAPIView):
    queryset = ETS.objects.all()
    serializer_class = ETSSerializer

class Alumno_ETSListCreate(generics.ListCreateAPIView):
    queryset = Alumno_ETS.objects.all()
    serializer_class = Alumno_ETSSerializer

class Tipo_tramiteListCreate(generics.ListCreateAPIView):
    queryset = Tipo_tramite.objects.all()
    serializer_class = Tipo_tramiteSerializer

class TramiteListCreate(generics.ListCreateAPIView):
    queryset = Tramite.objects.all()
    serializer_class = TramiteSerializer

class Tipo_archivoListCreate(generics.ListCreateAPIView):
    queryset = Tipo_archivo.objects.all()
    serializer_class = Tipo_archivoSerializer

class Archivo_adjuntoListCreate(generics.ListCreateAPIView):
    queryset = Archivo_adjunto.objects.all()
    serializer_class = Archivo_adjuntoSerializer

