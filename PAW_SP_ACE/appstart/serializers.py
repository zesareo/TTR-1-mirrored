from rest_framework import serializers
from .models import Usuario,Alumno,Agente,Materia,ETS,Alumno_ETS,Tipo_tramite,Tramite,Tipo_archivo,Archivo_adjunto

class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = ('id','rol','correo','contrasena','paterno','materno','nombre','nacimiento','telefono','domicilio')

class AlumnoSerializer(serializers.ModelSerializer):
    """
    A usuer serializer to return the user details
    """
    usuario = UsuarioSerializer(required=True)
    class Meta:
        model = Alumno
        fields = ('usuario','boleta','curp','fecha_ingreso')

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = Usuario.objects.create(**usuario_data)
        alumno = Alumno.objects.create(usuario = usuario, **validated_data)
        return alumno

class AgenteSerializer(serializers.ModelSerializer):
    """
    A usuer serializer to return the user details
    """
    usuario = UsuarioSerializer(required=True)
    class Meta:
        model = Agente
        fields = ('usuario','folio')

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = Usuario.objects.create(**usuario_data)
        agente = Agente.objects.create(usuario = usuario, **validated_data)
        return agente

class MateriaSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Materia
        fields = ('id','nivel','nombre','carga')

class ETSSerializer(serializers.ModelSerializer):
    """
    A materia serializer to return the materia details
    """
    materia = MateriaSerializer(read_only = False)
    class Meta:
        model = ETS
        fields = ('turno','precio','materia')

    def create(self, validated_data):
        materias_data = validated_data.pop('materia')
        materia = Materia.objects.create(**materias_data)
        ets = ETS.objects.create(materia = materia, **validated_data)
        return ets
        
class Alumno_ETSSerializer(serializers.ModelSerializer):
    """
    A alumno & ets serializer to return the alumno & ets details
    """
    alumno = AlumnoSerializer(read_only=False)
    ets = ETSSerializer(read_only=False)
    #alumno = serializers.PrimaryKeyRelatedField(read_only=False)
    #ets = serializers.PrimaryKeyRelatedField(read_only=False)
   
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
