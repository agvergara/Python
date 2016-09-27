#!/usr/bin/python

#
# webApp class
# Root for hierarchy of classes implementing web applications
#
# Copyright Jesus M. Gonzalez-Barahona 2009
# jgb @ gsyc.es
# TSAI and SAT subjects (Universidad Rey Juan Carlos)
# October 2009
#

import socket

class webApp(object):
    """Root of a hierarchy of classes implementing web applications
    This class does almost nothing. Usually, new classes will
    inherit from it, and by redefining "parse" and "process" methods
    will implement the logic of a web application in particular.
    """
    def parse (self, request):
        """Parse the received request, extracting the relevant information."""

        return None

    def process (self, parsedRequest):
        """Process the relevant elements of the request.
        Returns the HTTP code for the reply, and an HTML page.
        """

        return ("200 OK", "<html><body><h1>It works!</h1></body></html>")

    def __init__ (self, hostname, port):
        """Initialize the web application."""

        # Create a TCP objet socket and bind it to a port
        mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((hostname, port))

        # Queue a maximum of 5 TCP connection requests
        mySocket.listen(5)

        # Accept connections, read incoming data, and call
        # parse and process methods (in a loop)
        while True:
            print 'Waiting for connections'
            (recvSocket, address) = mySocket.accept()
            print 'HTTP request received (going to parse and process):'
            request = recvSocket.recv(2048)
            print request
            try:
                parsedRequest = self.parse (request)
            except IndexError:
              continue
            except ValueError:
                recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body><h1>Muy gracioso con el char</h1></body></html>\r\n")
                continue
            (returnCode, htmlAnswer) = self.process (parsedRequest)
            print 'Answering back...'
            recvSocket.send("HTTP/1.1 " + returnCode + " \r\n\r\n"
                             + htmlAnswer + "\r\n")
            recvSocket.close()

class calculApp (webApp):

    def parse(self, request):
        numEntero = float(request.split()[1][1:])
        return numEntero

    def process(self, parsedRequest):
        if self.firstInt == None:
            self.firstInt = parsedRequest
            htmlAnswer = ("<html><body><h1>Sumas con clase!</h1><p> Me has enviado: " +
                        str(self.firstInt) + "</p></body></html>")
        else:
            resultado = str(self.firstInt + parsedRequest)
            htmlAnswer = ("<html><body><h1>Sumas con clase!</h1>" +
                         "<p> El resultado de: " + str(self.firstInt) + " + " + str(parsedRequest) +
                         " es: " + resultado + "</p></body></html>")
            self.firstInt = None
        return ("200 OK", htmlAnswer)

    def __init__(self, hostname, port):
        self.firstInt = None
        super(calculApp, self).__init__(hostname, port)

if __name__ == "__main__":
    testWebApp = calculApp ("localhost", 1234)
