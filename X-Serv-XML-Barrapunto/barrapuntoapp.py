#!/usr/bin/python
# -*- coding: utf-8 -*-

#XML Parser given an url

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import urllib2
import os

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
                self.html += ("<a href=" + self.link + ">" + self.title +
                              "</a><br/><hr><br/>")
                self.title = ""
                self.link = ""

    def endDocument(self):
            htmlfile = open('htmlfile.html', 'w')
            self.html = self.html.encode('utf-8')
            htmlfile.write("<html><body>" + self.html + "</body></html>")
            htmlfile.close()


    def characters (self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars

#Main program
if len(sys.argv)<2:
    print "Usage: python barrapuntoapp.py <url>"
    print
    print " <url>: url name of the document to parse"
    sys.exit(1)

# Load parser and driver
theParser = make_parser()
theHandler = myContentHandler()
theParser.setContentHandler(theHandler)

try:
    xmlbody = urllib2.urlopen(sys.argv[1]).read()
    xmlfile = open('rssfile.rss', 'w')
    xmlfile.write(xmlbody)
    xmlfile.close()
except ValueError:
    print "Could not open url"
    sys.exit(1)

xmlfile = open('rssfile.rss', 'r')
theParser.parse(xmlfile)

os.system("firefox ./htmlfile.html")
