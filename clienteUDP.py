from socket import *

from pip._vendor.distlib.compat import raw_input

###
# Cadena de caracteres que contiene la direccion IP del servidor o el nombre del host
# Si se utiliza el nombre del host, se llevará automaticamente una busqueda DNS para obtener la direccion IP
###
serverName = 'localhost'

###
# Asigna el valor del puerto para la conexion
##
serverPort = 8050

###
# Se Crea el cliente del socket
# AF_INET --> Indica que la red subyacente esta utilizando IPv4
# SOCK_DGRAM --> Especifica que se trata de un socket UDP
# NO se especifica el puerto a utilizar, dejamos que el sistema operativo lo haga
###
clientSocket = socket(AF_INET, SOCK_DGRAM)


###
# raw_input --> funcion para la incorpracion de texto
##
message = raw_input('Escriba una frase en minuscula: ')

### ENVIO DEL SOCKET HACIA EL HOST DESTINO
# encode() --> funcion para convertir la cadena a byte
# sendto() --> asocia la direccion de destino al mensaje y envia el paquete por el socket, clientsocket
###
clientSocket.sendto(message.encode(), (serverName, serverPort))

###
# Cuando un paquete procedente de Internet llega al socket del cliente, los datos se almacenan en la valiable modifiedMessage
# La dirección origen del paquete se almacena en serverAddress (contiene la direc. IP del servidor y el numero de puerto del mismo
###
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())

###
# Cierra el socket y termina el proceso
###
clientSocket.close()
