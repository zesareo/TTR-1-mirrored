from rest_framework import serializers
from .models import Usuario,Alumno,Agente,Materia,ETS,Tipo_tramite,Tramite,Tipo_archivo,Archivo_adjunto,Alumno_ETS
from django.contrib.auth.models import User

import qrcode
#import firma_FULL as F
#import cifradoFuncion as CF

from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

from Crypto import Random
from Crypto.PublicKey import RSA
import binascii
from Crypto.Cipher import PKCS1_OAEP

import qrcode

def get_hash(resource_path):
    
    sha = SHA256.new()
    #with open(resource_path, 'rb') as file:    #Django ya lo abre
    file = resource_path
    while True:
        # Reading is buffered, so we can read smaller chunks.
        chunk = file.read(sha.block_size)
        if not chunk:
            break
        sha.update(chunk)
    print('\nHASH DEL DOCUMENTO:') 
    print(sha.hexdigest())

    return sha


def genera_qr(llave_publica, nombre_documento):
    
    imagen = qrcode.make(llave_publica)
    archivo_imagen = open(nombre_documento+'.png', 'wb')
    imagen.save(archivo_imagen)
    archivo_imagen.close()


def generar_llaves():

    random_generator = Random.new().read

    private_key = RSA.generate(1024, random_generator)
    public_key = private_key.publickey()

    llaves = [private_key,public_key]

    return llaves

#Firmar
def firmar(llaves, resource):

    #signer = PKCS1_v1_5.new(llaves.private_key) #firmante
    signer = PKCS1_v1_5.new(llaves[0]) #firmante

    #sha = SHA256.new()
    #sha.update(resource)
    sha = get_hash(resource)

    print('\nHash origen --Auth')
    print(sha.hexdigest())

    signature = signer.sign(sha) #Firma = MAC
    
    print('\nMAC (Message Auth Code) = Hash + clave   ---integridad y auth')
    print(signature)

    return signature
    
#verificar Firma
def verificarMAC(llave_publica, resource, firma):

    user = PKCS1_v1_5.new(llave_publica) #usuario 

    #sha = SHA256.new()
    #sha.update(resource) 
    sha = get_hash(resource)

    print('\nHash destino --Auth')
    print(sha.hexdigest())

    result = user.verify(sha, firma)
    
    print('\nComprueba MAC')
    print(result)

    return result


class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = ['id','rol','correo','contrasena','paterno','materno','nombre','nacimiento','telefono','domicilio']


class AlumnoSerializer(serializers.ModelSerializer):
    """
    A usuer serializer to return the user details
    """
    usuario = UsuarioSerializer(required=True)
    
    class Meta:
        model = Alumno
        fields = ['usuario','boleta','curp','fecha_ingreso']
        
        
    def create(self, validated_data):
        try:        
            #Crear usuario
            usuario_data = validated_data.pop('usuario')
            usuario = Usuario.objects.create(**usuario_data)
            #Crear alumno1
            alumno = Alumno.objects.create(usuario = usuario, **validated_data)
            #Crear user
            user = validated_data.pop('boleta')
            passw = usuario_data.pop('contrasena')
            correo = usuario_data.pop('correo')

            user = User.objects.create_user(user, correo, passw)
            user.save()
                
        except: print('Ocurrio un error')    
        return alumno

    def update(self,instance, validated_data):
        '''
        usuario.id
        usuario.rol
        ...
        boleta
        '''
        try:
            usuario_data = validated_data.pop('usuario')
            #usuario = Usuario.objects.create(**usuario_data)
            usuario = instance.usuario
            
            #Actualiza agente
            instance.boleta = validated_data.get('boleta', instance.boleta)
            instance.curp = validated_data.get('curp', instance.curp)
            instance.fecha_ingreso = validated_data.get('fecha_ingreso', instance.fecha_ingreso)
            instance.save()

            #Actualiza usuario
            #'correo','paterno','materno','nombre','nacimiento','telefono','domicilio'
            usuario.correo = usuario_data.get( 'correo', usuario.correo)
            usuario.paterno = usuario_data.get( 'paterno', usuario.paterno)
            usuario.materno = usuario_data.get( 'materno', usuario.materno)
            usuario.nombre = usuario_data.get( 'nombre', usuario.nombre)
            usuario.nacimiento = usuario_data.get( 'nacimiento', usuario.nacimiento)
            usuario.telefono = usuario_data.get( 'telefono', usuario.telefono)
            usuario.domicilio = usuario_data.get( 'domicilio', usuario.domicilio)
            usuario.save()

            '''
            usuario_list = []
            for usuario in usuario_data:
                usuario, created = Usuario.objects.get_or_create(rol = usuario['rol'])
                usuario_list.append(usuario)
            '''
            #instance.usuario = usuario
            #instance.save()
        
        except: print('Ocurrio un error') 
        return instance
        
        

class AgenteSerializer(serializers.ModelSerializer):
    """
    A usuer serializer to return the user details
    """
    usuario = UsuarioSerializer(required=True)
    class Meta:
        model = Agente
        fields = ['usuario','folio']

    def create(self, validated_data):
        try:
            #Crear usuario
            usuario_data = validated_data.pop('usuario')
            usuario = Usuario.objects.create(**usuario_data)
            #Crear Agente
            agente = Agente.objects.create(usuario = usuario, **validated_data)
            #Crear user
            user = validated_data.pop('folio')
            passw = usuario_data.pop('contrasena')
            correo = usuario_data.pop('correo')
            is_staff = True
            is_superuser = False
            
            user = User.objects.create_user(user, correo, passw)
            #user = User.objects.create_superuser(user, correo, passw, is_staff, is_superuser)
            user.save()
            user.is_staff = True
            user.save()

        except: print('Ocurrio un error') 
        return agente

    def update(self,instance, validated_data):
        try:
            '''
            usuario.id
            usuario.rol
            ...
            boleta
            '''
            usuario_data = validated_data.pop('usuario')
            #usuario = Usuario.objects.create(**usuario_data)
            usuario = instance.usuario
            
            #Actualiza agente
            instance.folio = validated_data.get('folio', instance.folio)
            instance.save()

            #Actualiza usuario
            #'correo','paterno','materno','nombre','nacimiento','telefono','domicilio'
            usuario.correo = usuario_data.get( 'correo', usuario.correo)
            usuario.paterno = usuario_data.get( 'paterno', usuario.paterno)
            usuario.materno = usuario_data.get( 'materno', usuario.materno)
            usuario.nombre = usuario_data.get( 'nombre', usuario.nombre)
            usuario.nacimiento = usuario_data.get( 'nacimiento', usuario.nacimiento)
            usuario.telefono = usuario_data.get( 'telefono', usuario.telefono)
            usuario.domicilio = usuario_data.get( 'domicilio', usuario.domicilio)
            usuario.save()

            #instance.usuario=usuario
            #instance.save
            
        except: print('Ocurrio un error') 
        return instance
    


class MateriaSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Materia
        fields = ['id','nivel','nombre','carga']
    
    '''
    etss = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Materia
        fields = ['id','nivel','nombre','carga','etss']
    '''


class ETSSerializer(serializers.ModelSerializer):
    """
    A materia serializer to return the materia details
    """
    #materia = MateriaSerializer(read_only = False)
    #materia = serializers.StringRelatedField(many=True)
   
    class Meta:
        model = ETS
        fields = ['id','turno','precio','materia','fecha','estatus']
     

class Alumno_ETSSerializer(serializers.ModelSerializer):
    
    #A alumno & ets serializer to return the alumno & ets details
    
    class Meta:
        model = Alumno_ETS
        fields = ['id','alumno','ets']


class Tipo_tramiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_tramite
        fields = ['id','nombre']

class TramiteSerializer(serializers.ModelSerializer):
    #alumno = AlumnoSerializer(many=True, read_only=True)
    #tipo_tramite = Tipo_tramiteSerializer(many=True, read_only=True)
    #firma = serializers.SerializerMethodField()

    class Meta:
        model = Tramite
        fields = ['id','alumno','tipo_tramite','fecha_solicitud','ciclo_escolar','estatus','documento_firmado','comentario','atributos_dictamen','qr','firma']
    
    '''
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = TramiteSerializer(queryset, many=True)
        return Response(serializer.data)
    '''
    #Agente solo actualiza el estatus,documento,comentario
    def update(self,instance, validated_data):
        
        estatus = validated_data.get('estatus', instance.estatus)
        if (estatus != 'FINALIZADO'):

            documento_firmado = validated_data.get('documento_firmado', instance.documento_firmado)
            comentario = validated_data.get('comentario', instance.comentario)
            estatus = validated_data.get('estatus', instance.estatus)

            #Firmar
            llaves = generar_llaves()
            resource = documento_firmado
            firma = firmar(llaves,resource)

            #Formato ACSCII
            llave_publica = llaves[1].exportKey(format='DER')
            llave_publica_acsii = binascii.hexlify(llave_publica).decode('utf8')
            firma_ascii = binascii.hexlify(firma).decode('utf8') 

            #Actualizo
            instance.documento_firmado = documento_firmado
            instance.comentario = comentario
            instance.estatus = estatus
            instance.qr = llave_publica_acsii
            instance.firma= firma_ascii
            instance.save()

        return instance
    
    '''
    def update(self,instance, validated_data):
        
        #alumno.id
        #tipo_tramite.id
        #...
        #fecha_solicitud
        
        random_generator = Random.new().read

        #Keys
        private_key = RSA.generate(1024, random_generator)
        public_key = private_key.publickey()
        
        #QR
        img = qrcode.make('api/appstart/v2/Documento_Firmado/'+public_key)
        
        #Modulo de criptografia y almacenamiento de llave publica en QR
        #1.Obtener Documento
        
        documento_data = validated_data.pop('documento_firmado')
        
        #2.Cifrar 
        
        #firma
        signer = PKCS1_v1_5.new(private_key)
        
        #resource = 'Texto plano!'
        resource = documento_data
        resource = resource.encode()  #CODIFICAR = ENCRIPTAR  --- BASE DE DATOS 

        sha = SHA256.new()     #HASH
        sha.update(resource)

        signature = signer.sign(sha)   #A;ADE LA FIRMA AL DOCUMENTO QUE GENERAMOS HASH  

        instance.documento_firmado = resource ##RESOURCE deberia ser un objeto de tipo documento_firmado
        instance.documento_hash = signature ##SIGNATURE deberia ser un objeto de tipo documento_hash 
        instance.save()
        
        #3.Hash para dar validez al documento.
        
        signer = PKCS1_v1_5.new(public_key)   #QR

        sha = SHA256.new()
        sha.update(resource) #Recurso QUE VIENE CODIFICADO

        result = signer.verify(sha, signature)
        print(result)
        

        
        #1. El administrador puede verificar la autenticidad de un documento digital, escanearia el qr(llave publica) y compara con el documento desencifraria el documento.
       
        
        
        return instance
    '''

class Tramite_REACTSerializer(serializers.ModelSerializer):
    #alumno = AlumnoSerializer(many=True, read_only=True)
    #tipo_tramite = Tipo_tramiteSerializer(many=True, read_only=True)
    #firma = serializers.SerializerMethodField()

    class Meta:
        model = Tramite
        fields = ['id','documento_firmado','qr','firma']
    
    '''
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = TramiteSerializer(queryset, many=True)
        
        return Response(serializer.data)
    '''


class Tipo_archivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_archivo
        fields = ['id','nombre']

class Archivo_adjuntoSerializer(serializers.ModelSerializer):
    #tramite = TramiteSerializer(many=True, read_only=True)
    #tipo_archivo = Tipo_archivoSerializer(many=True, read_only=True)
    class Meta:
        model = Archivo_adjunto
        fields = ['id','tramite','tipo_archivo','documento']


class Alumno_ETSDescripcionSerializer(serializers.ModelSerializer):
    
    #A alumno & ets serializer to return the alumno & ets details
    
    alumno = AlumnoSerializer(read_only=True)
    ets = ETSSerializer(read_only=True)  
   
    class Meta:
        model = Alumno_ETS
        fields = ['id','alumno','ets']

class TramiteFase1Serializer(serializers.ModelSerializer):
    #alumno = AlumnoSerializer(many=True, read_only=True)
    #tipo_tramite = Tipo_tramiteSerializer(many=True, read_only=True)
    class Meta:
        model = Tramite
        fields = ['id','alumno','tipo_tramite','fecha_solicitud','ciclo_escolar','atributos_dictamen']



'''
class Documento_FirmadoSerializer(serializers.ModelSerializer):
    llavePublica = 
    class Meta:
        model = Tramite
        fields = []
'''