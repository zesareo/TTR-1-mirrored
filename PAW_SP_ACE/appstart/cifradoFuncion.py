'''
Crypto Tested in cPython 2.7.x, 3.4.x, and pypy 2.6.x (Python version 2.7.9)
Python versiones superiores usar pycryptodome 
'''
##CIFRADO 
from Crypto import Random
from Crypto.PublicKey import RSA
import binascii
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

def get_resource():
    return ('Hola mundo'.encode())

def generar_llaves():

    random_generator = Random.new().read

    private_key = RSA.generate(1024, random_generator)
    public_key = private_key.publickey()

    llaves = [private_key,public_key]

    return llaves

#Codificar a binario
def toBinaryCode(llaves):

    #private_key = private_key.exportKey(format='DER')
    private_key = llaves[0].exportKey(format='DER')

    #public_key = public_key.exportKey(format='DER')
    public_key = llaves[1].exportKey(format='DER')

    print('---------public key binario----------')
    print(public_key)

    llaves = [private_key, public_key]
    
    return llaves 

##codificar de binario a ascii
def binaytoASCII(llaves):
    
    #private_key = binascii.hexlify(private_key).decode('utf8')
    private_key = binascii.hexlify(llaves[0]).decode('utf8')
    
    #public_key = binascii.hexlify(public_key2).decode('utf8')
    public_key = binascii.hexlify(llaves[1]).decode('utf8')
    
    print('---------public key ascii----------')
    print(public_key)

    llaves = [private_key,public_key]

    return llaves

##Retornar al objeto llave desde ascii
def asciiToKey(llaves):
    
    #private_key = RSA.importKey(binascii.unhexlify(private_key))
    private_key = RSA.importKey(binascii.unhexlify(llaves[0]))

    #public_key = RSA.importKey(binascii.unhexlify(public_key))
    public_key = RSA.importKey(binascii.unhexlify(llaves[1]))
    
    print('--------public key original-------')
    print(public_key)

    llaves = [private_key, public_key]
    
    return llaves

#Cifrado
def cifraMensaje(resource, llave_publica):

    message = resource

    cipher = PKCS1_OAEP.new(llave_publica)
    encrypted_message  = cipher.encrypt(message)

    print('--------mensaje cifrado-------')
    print(encrypted_message)

    return encrypted_message

#Descifrado
def descifrarMensaje(encrypted_message, llave_privada):
    
    cipher = PKCS1_OAEP.new(llave_privada)
    message = cipher.decrypt(encrypted_message)
    
    print('--------mensaje cifrado-------')
    print(message)


#Ejemplo
'''
llaves = generar_llaves()
llaves_binario =toBinaryCode(llaves)
llaves_ascii = binaytoASCII(llaves_binario)
llaves_original = asciiToKey(llaves_ascii)

resource = get_resource()

mensaje_cifrado = cifraMensaje(resource, llaves[1]) 
descifrarMensaje(mensaje_cifrado, llaves[0])
'''