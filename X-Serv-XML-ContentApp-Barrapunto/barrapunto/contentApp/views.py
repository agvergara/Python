from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from barrapuntoapp import getRss
from models import Content
# Create your views here.

def getContentList(request):
	template = get_template('index.html')
	if request.path == '/update':
		ans = "Rss updated"
	elif request.path == '/':
		ans = "Main Page"
	rss = getRss()
	return HttpResponse(template.render (Context ({'page' : ans,
												   'list': rss})))
@csrf_exempt
def showContent(request, resource):
	if request.method == "GET":
		try:
			template = get_template('index.html')
			content = Content.objects.get(name=resource)
			rss = getRss()
			return HttpResponse(template.render (Context ({'page' : content.content,
														   'list': rss})))
		except Content.DoesNotExist:
			template = get_template('notfound.html')
			return HttpResponseNotFound(template.render())
	elif request.method == "PUT":
		addContent = Content (name=resource, content=request.body)
		addContent.save()
		template = get_template('urlans.html')
		return HttpResponse(template.render())
	else:
		return HttpResponseNotAllowed("Method not allowed")