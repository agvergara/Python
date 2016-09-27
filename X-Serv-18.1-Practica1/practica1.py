#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
 acortApp class
 URL shortener
 Antonio Gomez Vergara IST - 2016
"""

import webapp
import csv
import urllib


class acortApp (webapp.webApp):

    def insertUrl(self, flag, cuerpo):
        if flag is False:
            self.diccUrl[cuerpo] = self.contador
            self.diccRedir[self.contador] = cuerpo
            htmlAns = ("<html><body><h1>Acortador URLs</h1>" +
                       "<p> Me has pedido acortar: " +
                       "<a href=" + cuerpo + ">" + cuerpo + "</a>" +
                       " y esta es tu nueva url:" +
                       "<a href=http://localhost:1234/" +
                       str(self.contador) + ">" +
                       "http://localhost:1234/" + str(self.contador) +
                       "</a></p></body></html>")
            self.contador = self.contador + 1
        else:
            htmlAns = ("<html><body><h1>Acortador URLs</h1>" +
                       "<p> Ya me pediste acortar esa URL " +
                       "y la url asociada es: " +
                       "<a href=http://localhost:1234/" +
                       str(self.diccUrl[cuerpo]) + ">" +
                       "http://localhost:1234/" +
                       str(self.diccUrl[cuerpo]) +
                       "</a></p></body></html>")
        returnCode = "200 Ok"
        header = ""
        return (returnCode, htmlAns, header)

    def searchUrl(self, indice):
        try:
            htmlAns = ''
            header = ("Location: " + self.diccRedir[str(indice)]) + "\r\n"
            returnCode = "302 Found"
        except KeyError:
            returnCode = "404 Not Found"
            header = ""
            htmlAns = "<html><body><h1> 404 Not Found </h1></body></html>"
        return (returnCode, htmlAns, header)

    def parse(self, request):
        urlEntera = None
        metodo = request.split(' ', 2)[0]
        recurso = request.split(' ', 2)[1]
        try:
            cuerpo = urllib.unquote(request.split('\r\n\r\n')[1])
            cuerpo = cuerpo.split('=')[1]
            http = cuerpo.split(':')
        except IndexError:
            cuerpo = ""
            http = ""
        if recurso != 'favicon.ico':
            if len(http) < 2:
                urlEntera = "http://" + cuerpo
            else:
                urlEntera = cuerpo
        else:
            pass
        return metodo, recurso, urlEntera

    def process(self, parsedRequest):
        flag = False
        contador = 0
        metodo, recurso, cuerpo = parsedRequest
        if metodo == "GET":
            htmlAns = ("<html><body><h1>Acortador URLs</h1>" +
                       "<form method='POST' action=''>" +
                       "URL a acortar: <input type='text' name=url>" +
                       "<input type='submit' value='Enviar'>" +
                       "</form></body></html>")
            returnCode = "200 Ok"
            header = ""
            try:
                recurso = int(recurso.split('/')[1])
                (returnCode, htmlAns, header) = self.searchUrl(recurso)
            except (ValueError):
                pass
                #Si me piden el recurso /0 (por ejemplo) se redirige, mientras
                #que si me piden un recurso /www.algo.com devuelve otra vez
                #el formulario
        elif metodo == "POST":
            if cuerpo != "http://":
                if recurso is not None:
                    for url in self.diccUrl:
                        if cuerpo == url:
                            flag = True
                            break
                    (returnCode, htmlAns, header) = self.insertUrl(flag, cuerpo)
                else:
                    returnCode = "204 No content"
                    htmlAns = ""
                    header = ""
            else:
                returnCode = "400 Bad Request"
                htmlAns = ("<html><body><h1> 400 Bad Request </h1>" +
                           "<p>Empty QS</p></body></html>")
                header = ""
        else:
            returnCode = "405 Method Not Allowed"
            htmlAns = ("<html><body><h1> 405 Method Not Allowed </h1>" +
                       "<p>Only support GET and POST methods</p>" +
                       "</body></html>")
            header = ""
        return (returnCode, htmlAns, header)

    def __init__(self, hostname, port):
        self.contador = 0
        self.diccUrl = {}
        self.diccRedir = {}
        try:
            with open('redirecting.csv', 'r') as csvfile:
                urlreader = csv.reader(csvfile)
                for rows in urlreader:
                    try:
                        self.diccRedir[rows[0]] = rows[1]
                        self.diccUrl[rows[1]] = rows[0]
                    except IndexError:
                        pass
                for index in self.diccRedir:
                    if self.contador <= int(index):
                        self.contador = int(index)
                self.contador = self.contador + 1
        except IOError:
            #Si el fichero "redirecting.csv" no existe, lo crea al iniciar y
            #luego ya utiliza ese mismo fichero
            filecreat = open('redirecting.csv', 'w')
            filecreat.close()
        try:
            super(acortApp, self).__init__(hostname, port)
        except KeyboardInterrupt:
            with open('redirecting.csv', 'w') as csvfile:
                urlwriter = csv.writer(csvfile)
                for key, value in self.diccRedir.items():
                    urlwriter.writerow([key, value])

if __name__ == "__main__":
    testWebApp = acortApp("localhost", 1234)
