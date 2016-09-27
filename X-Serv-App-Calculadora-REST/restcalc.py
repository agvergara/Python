#!/usr/bin/python

"""
restCalc class
 REST-type calculator
 Antonio Gomez Vergara IST
"""

import webapp


class restCalc(webapp.webApp):

	def parse(self, request):

		method = request.split(' ', 2)[0]
		resource = request.split(' ', 2)[1][1:]
		body = request.split('\r\n\r\n')[1]
		print "Method: " + method
		print "Resource: " + resource
		print "Body: " + body
		return (method, resource, body)

	def process(self, parsedRequest):

		method, resource, body = parsedRequest

		httpCode = "200 Ok"
		if method == "GET":
			htmlAnswer = ("<html><body><p>Resultado anterior:" + 
						   self.respuesta + 
                           "</body></html>")
		elif method == "PUT":
			operators = body.split(' ', 2)
			num1 = int(operators[0])
			num2 = int(operators[2])
			optype = operators[1]
			if optype == "+":
				self.result = str(num1 + num2)
				self.respuesta = str(num1) + " + " + str(num2) + " = " + self.result
			elif optype == "-":
				self.result = str(num1 - num2)
				self.respuesta = str(num1) + " - " + str(num2) + " = " + self.result
			elif optype == "*":
				self.result = str(num1 * num2)
				self.respuesta = str(num1) + " * " + str(num2) + " = " + self.result
			elif optype == "/":
				try:
					self.result = str(num1 / num2)
				except ZeroDivisionErrror:
					self.result = "Divided by 0"
				self.respuesta = str(num1) + " / " + str(num2) + " = " + self.result
			htmlAnswer = "<html><body><h1>" + self.respuesta + "</h1></body></html>"
		else:
			httpCode = "405 Method Not Allowed"
			htmlAnswer = "<html><body><h1>" + httpCode + "</h1></body></html>"

		return (httpCode, htmlAnswer)

if __name__ == '__main__':
	try:
		calculator = restCalc("localhost", 1234)
	except KeyboardInterrupt:
		print "Closing server..."
