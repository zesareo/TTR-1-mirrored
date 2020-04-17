from rest_framework import serializers
from .models import Usuario,Alumno,Agente,Materia,ETS,Alumno_ETS,Tipo_tramite,Tramite,Tipo_archivo,Archivo_adjunto

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('rol','correo','contrasena','paterno','materno','nombre','nacimiento','telefono','domicilio')

class AlumnoSerializer(serializers.ModelSerializer):
    """
    A usuer serializer to return the user details
    """
    usuario = UsuarioSerializer(required=True)
    class Meta:
        model = Alumno
        fields = ('usuario','boleta','curp','fecha_ingreso')

class AgenteSerializer(serializers.ModelSerializer):
    """
    A usuer serializer to return the user details
    """
    usuario = UsuarioSerializer(required=True)
    class Meta:
        model = Agente
        fields = ('usuario','folio')

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = ('nivel','nombre','carga')

class ETSSerializer(serializers.ModelSerializer):
    #materia = serializers.RelatedField(source='materia', read_only=True)
    materia = MateriaSerializer(many=True, read_only=True)
    class Meta:
        model = ETS
        fields = ('turno','precio','materia')

class Alumno_ETSSerializer(serializers.ModelSerializer):
    alumno = AlumnoSerializer(many=True, read_only=True)
    ets = MateriaSerializer(many=True, read_only=True)
    class Meta:
        model = Alumno_ETS
        fields = ('alumno','ets','fecha','estatus')

class Tipo_tramiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_tramite
        fields = ('nombre')

class TramiteSerializer(serializers.ModelSerializer):
    alumno = AlumnoSerializer(many=True, read_only=True)
    tipo_tramite = Tipo_tramiteSerializer(many=True, read_only=True)
    class Meta:
        model = Tramite
        fields = ('alumno','tipo_tramite','fecha_solicitud','ciclo_escolar','estatus','documento','comentario')

class Tipo_archivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_archivo
        fields = ('nombre')

class Archivo_adjuntoSerializer(serializers.ModelSerializer):
    tramite = TramiteSerializer(many=True, read_only=True)
    tipo_archivo = Tipo_archivoSerializer(many=True, read_only=True)
    class Meta:
        model = Archivo_adjunto
        fields = ('tramite','tipo_archivo','documento')