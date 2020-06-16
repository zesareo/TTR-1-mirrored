from django.shortcuts import render
from appstart.models import Usuario, Alumno, Agente, Materia, ETS, Alumno_ETS, Tipo_tramite, Tramite, Tipo_archivo, Archivo_adjunto
from appstart.serializers import UsuarioSerializer,AlumnoSerializer #,AgenteSerializer,MateriaSerializer,ETSSerializer,Alumno_ETSSerializer,Tipo_tramiteSerializer,TramiteSerializer,Tipo_archivoSerializer,Archivo_adjuntoSerializer
from rest_framework.permissions import IsAuthenticated

#Vistas basadas en clases && Vistas con clases genericas y mixins
'''
    -Los mixins ayudan a no tener que definir todos los metodos de la clase
    -Modify appstart/urls.py
    -as_view()
'''
from rest_framework.views import APIView   
from django.http import Http404            
from rest_framework import mixins, generics   
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

#VISTAS CON CLASES GENERICAS Y MIXINS

'''
    CRUD USUARIO
'''
class UsuarioMixin(object):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioList(UsuarioMixin, ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    pass
class UsuarioDetails(UsuarioMixin, RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    pass

'''
    CRUD ALUMNO
'''
class AlumnoMixin(object):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class AlumnoList(AlumnoMixin, ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    pass
class AlumnoDetails(AlumnoMixin, RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    pass