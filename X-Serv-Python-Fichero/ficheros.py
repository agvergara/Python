#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

fd = open("/etc/passwd", "r")
lineL = fd.readlines()

for line in lineL:
	elements = line.split(':')
	login = elements[0]
	shell = elements[-1][:-1]
	print "--User:", login, "--Shell:", shell
	
print "Hay", len(lineL), "users en esta maquina"
fd.close()
#Esto es una prueba2
