from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.utils.html import strip_tags
from models import Url

import urllib2
# Create your views here.

def shortener(request):
	flag = False
	local = "http://" + request.get_host() + "/"
	lista = ""
	if request.method == "GET":
		template = get_template("index.html")
		url_list = Url.objects.all()
		for url in url_list:
		lista += "<li><a href=/" + str(url.id) + ">" + url.original + "</a>"
		shorthis = ""
	elif request.method == "POST":
		body = request.body
		body = body.split('&')[1]
		shorthis = urllib2.unquote(body.split('=')[1])
		if shorthis != "":
			#Proteccion anti-XSS! Que me la lian
			shorthis = strip_tags(shorthis)
			try:
				shorthis = "https://" + shorthis.split('/', 2)[2]
				print shorthis
			except IndexError:
				shorthis = "https://" + shorthis
			url_list = Url.objects.all()
			for url in url_list:
				if url.original == shorthis:
					template = get_template('exists.html')
					local += str(url.id)
					flag = True
					break
			if not flag:
				urls = Url(original=shorthis)
				urls.save()
				template = get_template('urlans.html')
				urls = Url.objects.get(original=shorthis)
				local += str(urls.id)
		else:
			local = ""
			template = get_template('emptyqs.html')
			return HttpResponse(template.render())
	else:
		return HttpResponseNotAllowed("Method Not Allowed")
	context = RequestContext (request, {'original' : shorthis, 'acortada': local, 'lista' : lista})
	return HttpResponse(template.render(context))

def redirect (request, identifier):
	try:
		url = Url.objects.get(id=identifier)
		ans = url.original
	except ObjectDoesNotExist:
		template = get_template('notfound.html')
		return HttpResponseNotFound(template.render())
	return HttpResponseRedirect(ans)

def notfound (request):
	template = get_template('notfound.html')
	return HttpResponseNotFound(template.render())
