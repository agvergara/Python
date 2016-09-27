#!/usr/bin/python
# -*- coding: utf-8 -*-

#XML Parser given an url

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys

class myContentHandler(ContentHandler):

    def __init__ (self):
        self.inItem = False
        self.inContent = False
        self.endfile = False
        self.theContent = ""
        self.title = ""
        self.link = ""
        self.html = ""


    def startElement(self, name, attrs):
        if name == 'item':
            self.inItem = True
        elif self.inItem:
            if name == 'title':
                self.inContent = True
            elif name == 'link':
                self.inContent = True

    def endElement(self, name):
        if name == 'item':
            self.inItem = False
        elif self.inContent:
            if name == 'title':
                self.title = self.theContent
                self.inContent = False
                self.theContent = ""
            elif name == 'link':
                self.link = self.theContent
                self.inContent = False
                self.theContent = ""
            if self.title != "" and self.link != "":
                self.html += ("<li><a href=" + self.link + ">" + self.title +
                              "</a></li><br/>")
                self.title = ""
                self.link = ""

    def characters (self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars


#Returns the 'html' variable from 'myContentHandler'
def getRss():
    theParser = make_parser()
    theHandler = myContentHandler()
    theParser.setContentHandler(theHandler)
    theParser.parse("http://barrapunto.com/index.rss")
    return theHandler.html
