from django.shortcuts import render
from appstart.models import Usuario, Alumno, Agente, Materia, ETS, Alumno_ETS, Tipo_tramite, Tramite, Tipo_archivo, Archivo_adjunto,Alumno_ETS
from appstart.serializers import UsuarioSerializer,AlumnoSerializer ,AgenteSerializer,MateriaSerializer,ETSSerializer,Tipo_tramiteSerializer,TramiteSerializer,Tipo_archivoSerializer,Archivo_adjuntoSerializer,Alumno_ETSSerializer, Alumno_ETSDescripcionSerializer, TramiteFase1Serializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser 

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
    permission_classes = [IsAdminUser] #Solo agentes puedes ver detalles
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

'''
    CRUD AGENTE
'''
class AgenteMixin(object):
    queryset = Agente.objects.all()
    serializer_class = AgenteSerializer

class AgenteList(AgenteMixin, ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    pass
class AgenteDetails(AgenteMixin, RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    pass

'''
    CRUD Materia
'''
class MateriaMixin(object):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

class MateriaList(MateriaMixin, ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    pass
class MateriaDetails(MateriaMixin, RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    pass

'''
    CRUD ETS
'''
class ETSMixin(object):
    queryset = ETS.objects.all()
    serializer_class = ETSSerializer

class ETSList(ETSMixin, ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    pass
class ETSDetails(ETSMixin, RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    pass
'''
    CRUD Tipo Tramite
'''
class Tipo_tramiteMixin(object):
    queryset = Tipo_tramite.objects.all()
    serializer_class = Tipo_tramiteSerializer

class Tipo_tramiteList(Tipo_tramiteMixin, ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    pass
class Tipo_tramiteDetails(Tipo_tramiteMixin, RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    pass

'''
    CRUD Tramite
'''
class TramiteMixin(object):
    queryset = Tramite.objects.all()
    serializer_class = TramiteSerializer

class TramiteList(TramiteMixin, ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    pass
class TramiteDetails(TramiteMixin, RetrieveUpdateDestroyAPIView):
    #SOLO EL ADMINISTRADOR PUEDE HACER ESTA ACCION PARA CARGAR EL DOCUMENTO
    #permission_classes = (IsAuthenticated,)
    pass

'''
    Tramite Fase 1, no muestra documento
'''
class TramiteFase1Mixin(object):
    queryset = Tramite.objects.all()
    serializer_class = TramiteFase1Serializer

class TramiteFase1List(TramiteFase1Mixin, ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    pass

'''
    CRUD Tipo Archivo
'''
class Tipo_archivoMixin(object):
    queryset = Tipo_archivo.objects.all()
    serializer_class = Tipo_archivoSerializer

class Tipo_archivoList(Tipo_archivoMixin, ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    pass
class Tipo_archivoDetails(Tipo_archivoMixin, RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    pass

'''
    CRUD Archivo Adjunto
'''
class Archivo_adjuntoMixin(object):
    queryset = Archivo_adjunto.objects.all()
    serializer_class = Archivo_adjuntoSerializer

class Archivo_adjuntoList(Archivo_adjuntoMixin, ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    pass
class Archivo_adjuntoDetails(Archivo_adjuntoMixin, RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    pass
'''
    CRUD Alumno_ETS
'''
class Alumno_ETSMixin(object):
    queryset = Alumno_ETS.objects.all()
    serializer_class = Alumno_ETSSerializer

class Alumno_ETSList(Alumno_ETSMixin, ListCreateAPIView):
    pass
    #permission_classes = (IsAuthenticated,)
    
class Alumno_ETSDetails(Alumno_ETSMixin, RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    pass

#VISTA GENERICA FILTRADO
class Alumno_ETSBY(generics.ListCreateAPIView):
    queryset = Alumno_ETS.objects.all()
    serializer_class = Alumno_ETSSerializer
    
    def get_queryset(self):
           """
           This view should return a list of all models by
           the maker passed in the URL
           """
           maker = self.kwargs['alumno']
           #marker2 = self.kwargs['ets']
           return Alumno_ETS.objects.filter(alumno=maker)

class Alumno_ETSDescripcionBY(generics.ListCreateAPIView):
    queryset = Alumno_ETS.objects.all()
    serializer_class = Alumno_ETSDescripcionSerializer
    
    def get_queryset(self):
           """
           This view should return a list of all models by
           the maker passed in the URL
           """
           maker = self.kwargs['alumno']
           marker2 = self.kwargs['ets']
           return Alumno_ETS.objects.filter(alumno=maker, ets = marker2)

class Alumno_ETSDescripcion(generics.ListCreateAPIView):
    queryset = Alumno_ETS.objects.all()
    serializer_class = Alumno_ETSDescripcionSerializer


class TramiteBY(generics.ListCreateAPIView):
    queryset = Tramite.objects.all()
    serializer_class = TramiteFase1Serializer
    
    def get_queryset(self):
           """
           This view should return a list of all models by
           the maker passed in the URL
           """
           maker = self.kwargs['alumno']
           return Tramite.objects.filter(alumno=maker)








