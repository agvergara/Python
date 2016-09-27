from django.shortcuts import render
from models import Pages
from django.http import HttpResponse, HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def getcontent(request):
    content_list = Pages.objects.all()
    ans = "<ol>"
    for content in content_list:
        ans += "<li><a href=/content/" + str(content.id) + ">" + content.name + "</a>"
    ans += "</ol>"
    return HttpResponse(ans)

def searchcontent(request, identifier):
	try:
		content_line = Pages.objects.get(id=identifier)
		message = content_line.page
	except ObjectDoesNotExist:
		return HttpResponse("Does not exist")
	return HttpResponse(message)

def notfound (request):
	return HttpResponseNotFound("Not found")