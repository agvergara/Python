#!/usr/bin/python

"""
webApp class
 Root for hierarchy of classes implementing web applications
 Copyright Jesus M. Gonzalez-Barahona and Gregorio Robles (2009-2015)
 jgb @ gsyc.es
 TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
 October 2009 - February 2015
"""

import socket
import random

# Create a TCP objet socket and bind it to a port
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests
mySocket.listen(5)

# Accept connections, read incoming data
try:
    while True:
        numrand = str(random.randint(0, 99999999999999))
        url = "http://localhost:1234/" + numrand
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'HTTP request received:'
        print recvSocket.recv(1024)
        print 'Answering back...'
        recvSocket.send("HTTP/1.1 302 Moved Temporarily \r\n" + 
                        "Location: " + url + "\r\n" +
                        "<html><body><h1>Redirecciones por doquier!</h1>" +
                        "</body></html>" + "\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print "Stopping server"
    mySocket.close()