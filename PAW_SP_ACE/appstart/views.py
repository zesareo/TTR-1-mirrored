from django.shortcuts import render
from .models import Usuario, Alumno, Agente, Materia, ETS, Tipo_tramite, Tramite, Tipo_archivo, Archivo_adjunto
from .serializers import UsuarioSerializer,AlumnoSerializer,AgenteSerializer,MateriaSerializer,ETSSerializer,Tipo_tramiteSerializer,TramiteSerializer,Tipo_archivoSerializer,Archivo_adjuntoSerializer
from rest_framework import permissions, authentication

#Vistas basadas en funciones
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

#VISTAS GENERICAS
#class UsuarioListCreate(generics.ListCreateAPIView):
 #   queryset = Usuario.objects.all()
  #  serializer_class = UsuarioSerializer

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

'''
class Alumno_ETSListCreate(generics.ListCreateAPIView):
    queryset = Alumno_ETS.objects.all()
    serializer_class = Alumno_ETSSerializer
'''

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

#VISTAS BASADAS EN FUNCIONES

@api_view(['GET', 'POST'])
def usuario_list(request):
    """
    List all usuarios, or create a new usuario
    """
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UsuarioSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def usuario_details(request, pk):
    """
    Get, update, or delete a specific usuario
    """
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = UsuarioSerializer(usuario, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
#VISTAS CON CLASES Y MIXINS
'''

class UsuarioList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#List all Alumno, or create a new Alumno
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#VISTAS CON CLASES GENERICAS Y MIXINS

class UsuarioMixin(object):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioList(UsuarioMixin, ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)   
    #authentication_classes = ((authentication.SessionAuthentication, authentication.TokenAuthentication, authentication.BasicAuthentication))
    pass
class UsuarioDetails(UsuarioMixin, RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #authentication_classes = ((authentication.SessionAuthentication, authentication.TokenAuthentication, authentication.BasicAuthentication))
    pass
