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

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(("localhost", 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)
# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)
try:
    while True:
        numRandom = str(random.randint (0,300000000))
        url = "http://localhost:1234/" + numRandom
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        #(clientAddr, clientPort) = recvSocket.getpeername() Otra forma de sacar IP y puerto del cliente
        print 'HTTP request received:'
        print recvSocket.recv(1024)
        recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body><h1>Hola!</h1>" +
                        "<a href=" + url + "> Dame otra URL!" +
                        "</a>" +
                        "</body></html>" +
                        "\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print "Stopping server"
    mySocket.close()
