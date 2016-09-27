#!/usr/bin/python

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket
import random

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024
firstInt = None

def analyze (peticion, firstInt):
    numEntero = float(peticion.split()[1][1:])
    print firstInt
    if firstInt == None:
        firstInt = numEntero
        respuesta = "Me has enviado: " + str(firstInt)
    else:
        resultado = str(firstInt + numEntero)
        respuesta = "El resultado de: " + str(firstInt) + " + " + str(numEntero) + " es: " + str(resultado)
        firstInt = None
    return respuesta, firstInt

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(("localhost", 1234))

# Queue a maximum of 5 TCP connection requests
mySocket.listen(5)
# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)
# La funcion "analyze" devuelve una tupla donde el primer elemento es
#  la respueta que se envia y la segunda es el primer numero que el cliente
#  envia
try:
    while True:
        numRandom = str(random.randint (0,50))
        url = "http://localhost:1234/" + numRandom
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        #(clientAddr, clientPort) = recvSocket.getpeername() Otra forma de sacar IP y puerto del cliente
        print 'HTTP request received:'
        peticion = recvSocket.recv(1024)
        try:
            respuesta = analyze(peticion, firstInt)
            firstInt = respuesta[1]
        except IndexError:
            continue
        except ValueError:
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body><h1>Introduce un numero en la URL</h1></body></html>" + "\r\n")
            continue
        print 'Answering back...'
        recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body><h1>Numeros aleatorios!</h1>" +
                            "<a href=" + url + "> Para numero aleatorio! (0 - 50)" +
                            "</a>" +
                            "<p>" + respuesta[0] + "</p>"
                            "</body></html>" +
                            "\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print "Stopping server"
    mySocket.close()
