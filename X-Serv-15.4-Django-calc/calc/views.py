from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def suma(num1, num2):
	return num1 + num2

def resta(num1, num2):
	return num1 - num2

def mult (num1, num2):
	return num1 * num2

def div (num1, num2):
	try:
		resp = num1 / num2
	except ZeroDivisionError:
		resp = 'Divided by 0'
	return resp

def operations(request, num1, optype, num2):
	num1 = int(num1)
	num2 = int(num2)
	if optype == '+':
		ans = str(num1) + ' + ' + str(num2) + ' = ' + str(suma(num1,num2))
	elif optype == '-':
		ans = str(num1) + ' - ' + str(num2) + ' = ' + str(resta(num1,num2))
	elif optype == '*':
		ans = str(num1) + ' * ' + str(num2) + ' = ' + str(mult(num1,num2))
	elif optype == '/':
		ans = str(num1) + ' / ' + str(num2) + ' = ' + str(div(num1,num2))
	return HttpResponse(ans)


def error(request):
	return HttpResponse('404 Not Found')