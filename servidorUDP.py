from socket import *

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
serverSocket = socket(AF_INET, SOCK_DGRAM)


###
# Asociacion del numero de puerto al socket del servidor
###
serverSocket.bind(('', serverPort))

print('El servidor está listo para recibir')


while True:

    ###
    # Cuando un paquete llega al socket servidor,los datos se almacenan en clientAddress
    # clientAddresss --> contiene la direccion IP del cliente y el numero de puerto
    ###
    message, clientAddress = serverSocket.recvfrom(2048)

    modifiedMessage = message.decode().upper()

    ###
    # Asocia la direccion del cliente (IP y nº puerto) al mensaje escrito en mayuscula
    ###
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)