#!/usr/bin/python
# -*- coding: utf-8 -*-

# hola, hola

fd = open('/etc/passwd', 'r')

lineas = fd.readlines()
fd.close()
userdict = {} #Empty

for linea in lineas:
    elementos = linea.split(':')
    print elementos[0], elementos[-1][:-1]
    userdict[elementos[0]] = elementos[-1][:-1]
    
print "Hay", len(lineas), "usuarios en esta máquina"
usuarios = ['root', 'imaginario']
for usuario in usuarios:
    try:
        print "Para el usuario " + usuario + "la shell es: " + userdict[usuario]
    except (KeyError):
	print "Oops, para el user: " + usuario + "no hay entrada en el diccionario"
