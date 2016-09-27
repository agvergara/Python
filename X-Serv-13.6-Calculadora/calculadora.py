#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

if (len(sys.argv) != 4):
    sys.exit("Usage: ./calculadora.py operation int1 int2")

sumador = sys.argv[1]


def add(int1, int2):
    return int1 + int2


def sub(int1, int2):
    return int1 - int2


def multiply(int1, int2):
    return int1 * int2


def divide(int1, int2):
    try:
        return int1 / int2
    except ZeroDivisionError:
        print "No me intentes dividir entre cero"
        sys.exit()


try:
    int1 = float(sys.argv[2])
    int2 = float(sys.argv[3])
except ValueError:
    print "No me intentes operar con chars"
    sys.exit()

if sumador == "sumar":
    print str(int1) + " + " + str(int2) + " = " + str(add(int1, int2))
elif sumador == "restar":
    print str(int1) + " - " + str(int2) + " = " + str(sub(int1, int2))
elif sumador == "multiplicar":
    print str(int1) + " * " + str(int2) + " = " + str(multiply(int1, int2))
elif sumador == "dividir":
    print str(int1) + " / " + str(int2) + " = " + str(divide(int1, int2))
else:
    sys.exit("No se encuentra esa operacion")
