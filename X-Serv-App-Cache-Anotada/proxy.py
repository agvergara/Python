#!/usr/bin/python

#
# proxy class
# Class that works like a proxy
#

import webapp
import urllib2

class proxyApp (webapp.webApp):

	def addUrls (self, body, original_url):
		index1 = body.find("<body")
		index2 = body.find(">", index1)
		urls = ("<a href=http://" + original_url + "> Original Webpage </a>" +
				"<a href=/httpClient> Client-Side HTTP </a>" + 
				"<a href=/httpServer> Server-Side HTTP </a>" + 
				"<a href=/recargar/" + original_url + "> Refresh </a></br></br")
		fullBody = body[:index1] + urls + body[index2:]
		return fullBody

	def prettyHtml (self, string):
		return ("<html><body>" + string + "</body></html>")

	def parse(self, request):
		self.diccClient[self.contadorClient] = request
		self.contadorClient += 1
		try:
			resource = request.split(' ', 2)[1][1:]
		except IndexError:
			resource = ''
		return resource

	def process(self, resource):
		
		try:
			refresh = resource.split('/')[0]
			if refresh == "recargar":
				resource = resource.split('/')[1]
		except IndexError:
			pass

		if resource == "httpClient":
			httpCode = "200 Ok"
			httpBody = str(self.diccClient.items())
		elif resource == "httpServer":
			httpCode = "200 Ok"
			httpBody = str(self.diccServer.items())
		else:
			try:
				urlredir = urllib2.urlopen("http://" + resource)
				self.diccServer[self.contadorServer] = urlredir.info().headers
				self.contadorServer += 1
				httpBody = urlredir.read()
				httpBody = self.addUrls(httpBody, resource)
				httpCode = str(urlredir.getcode())
			except IOError:
				httpBody = "Could not connect"
				httpCode = "404 Not Found"
		#New requests
		self.diccServer = {}
		self.diccClient = {}
		self.contadorServer = 0
		self.contadorClient = 0
		return (httpCode, httpBody)

	def __init__ (self, hostname, port):
		self.contadorClient = 0
		self.contadorServer = 0
		self.diccClient = {}
		self.diccServer = {}
		self.urlOriginal = None
		try:
			super(proxyApp, self).__init__(hostname, port)
		except KeyboardInterrupt:
			print "Closing server. . ."

if __name__=="__main__":
	appProxy = proxyApp("localhost", 1234)