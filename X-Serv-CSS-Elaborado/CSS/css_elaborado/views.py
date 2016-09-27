from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotAllowed
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import get_template
from django.template import Context
from models import Pages
# Create your views here.

@csrf_exempt
def index(request, resource):
	cont_type = "text/html"
	if request.method == "GET":
		try:
			search = Pages.objects.get(name=resource)
			ans = search.content
			if search.name[0:3] == "css":
				cont_type = "text/css"
			else:
				template = get_template('index.html')
				return HttpResponse(template.render(Context({'content' : ans})), content_type='text/html')
		except ObjectDoesNotExist:
			return HttpResponse(resource + " does not exists")
	elif request.method == "PUT":
		body = request.body
		page = Pages(name=resource, content=body)
		page.save()
		ans = "Ok"
	else:
		return HttpResponseNotAllowed("Method not allowed")
	return HttpResponse(ans, content_type=cont_type)