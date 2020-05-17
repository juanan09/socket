from socket import *


serverPort = 8050

###
# Creacion por parte del servidor un socket TCP
###
serverSocket = socket(AF_INET, SOCK_STREAM)

###
# Asociacion del numero de puerto de servidor con este socket
###
serverSocket.bind(('', serverPort))

###
# Despues de establecer la puerta de entrada
# Esperar a escuchar que algun cliente llame a la puerta
# El parametro 1 indica el número maximo de conexiones en cola
###
serverSocket.listen(1)


print('El servidor esta listo para recibir')

while True:

    ###
    # Cuando un cliente llama a la puerta, el programa invoca el metodo accept()
    # Crea un nuevo socket en el servidor llamado connectionSocket, de este cliente en concreto
    # El cliente y servidor contemplan el acuerdo en 3 fases
    # Ahora ya pueden enviarse bytes entre si a traves de la misma.
    ###
    connectionSocket, adrr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())

    ###
    # Despues de enviar la frase modificada al cliente, se cierra el socket de conexion
    # Pero serverSocket queda abierto y por tanto otro cliente puede llamar a la puerta y enviar una nueva frase
    #
    connectionSocket.close()