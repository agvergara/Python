from django.shortcuts import render
from models import Pages
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import get_template
from django.template import Context

# Create your views here.

def getcontent(request):
    if request.user.is_authenticated():
        user = request.user.username
        template = get_template ("authent.html")
    else:
        user = ""
        template = get_template("notAuthent.html")

    content_list = Pages.objects.all()
    ans = ""
    for content in content_list:
        ans += "<li><a href=/annotated/content/" + str(content.id) + ">" + content.name + "</a>"
    return HttpResponse(template.render (Context ({'user': user,
                                                   'message': ans})))

def searchcontent(request, identifier):

    if request.user.is_authenticated():
        user = request.user.username
        template = get_template ("authent.html")
    else:
        user = ""
        template = get_template("notAuthent.html")
    content_list = Pages.objects.all()
    try:
        content_line = Pages.objects.get(id=identifier)
        ans = content_line.page
    except ObjectDoesNotExist:
        return HttpResponse("Does not exist")
    return HttpResponse(template.render (Context ({'user': user,
                                                   'message': ans})))

def notfound (request):
    return HttpResponseNotFound("Not found")

def redirect (request):
    return HttpResponseRedirect("http://localhost:8000/annotated/content/")
