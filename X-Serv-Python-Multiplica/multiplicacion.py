#!/usr/bin/python
# -*- coding: utf-8 -*-

for firstinteger in range(1,11):
    print ("Tabla del " + str(firstinteger) + "\n" + "---------------")
    for secondinteger in range(1,11):
        print (str(firstinteger) + " por " + str(secondinteger) + " es " + str(firstinteger * secondinteger))
    print "\n"
