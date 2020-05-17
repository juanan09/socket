from socket import *

from pip._vendor.distlib.compat import raw_input

serverName = 'localhost'
serverPort = 8050

## CREO UN CLIENTE ##
#El primer parametro indica que la red subyacente utilizada es IPv4
#El segundo parametro indica que es un socket de TCP
#No se especifica el puerto, el S.O lo hara por nosotros
###
clientSocket = socket(AF_INET, SOCK_STREAM)

### Inicio de la conexion Cliente-Servidor ###
# El metodo connect()
# Despues de su ejecucion se lleva a cabo el acuerdo en tres fases
# y se establece la conexion entre Cliente-Servidor
###
clientSocket.connect((serverName, serverPort))

sentence = raw_input('Escriba una frase en minuscula: ')

###
# Envio a traves del socket del cliente y la conexion TCP
# Coloca los byte de la cadena sentence en la conexion TCP
# El clienteespera a recibir los bytes procedentes del servidor
###
clientSocket.send(sentence.encode())

###
# Cuando llegan los caracteres del servidor, se colocan en la cedena modifiedSentence
# Los caracter se acumulan hasta que recibe un caracter de retorno de carro
#
modifiedSentence = clientSocket.recv(1024)

print('From Server: ', modifiedSentence.decode())

###
# Se cierra el socket y por tanto la conexion entre cliente-servidor
#
##clientSocket.close()