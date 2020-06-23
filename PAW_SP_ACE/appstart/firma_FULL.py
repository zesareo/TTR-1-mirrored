'''
Crypto Tested in cPython 2.7.x, 3.4.x, and pypy 2.6.x (Python version 2.7.9)
Python versiones superiores usar pycryptodome 
'''

from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

from Crypto import Random
from Crypto.PublicKey import RSA
import binascii
from Crypto.Cipher import PKCS1_OAEP

import qrcode

def get_hash(resource_path):
    
    sha = SHA256.new()

    with open(resource_path, 'rb') as file:   
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

#Firmar
'''
llaves = generar_llaves()
resource = 'api.docx'
firma = firmar(llaves,resource)

#1. Original
 
prueba1 =verificarMAC(llaves[1],resource,firma)

#2. Documento editado

resource2 = 'Ambiente.docx'

#resource2 = 'api.docx'

#Validacion de la firma
prueba2 = verificarMAC(llaves[1],resource2,firma)  #QR, DOCUMENTO, FIRMA = MAC


#3. Alguien mas firma el mismo documento pero yo lo valido con mi clave original
llaves2 = generar_llaves()
resource = 'api.docx'
firma2 = firmar(llaves2,resource)

#Validacion de la firma
prueba3 = verificarMAC(llaves[1],resource,firma2)
'''
