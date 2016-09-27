from django.shortcuts import render
from cms.models import Pages
from django.http import HttpResponse, HttpResponseNotAllowed
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def getform (request):
    if request.user.is_authenticated():
        user = request.user.username
        template = get_template("insert.html")
        context = RequestContext(request, {'user' : user})
    else:
        user = ""
        template = get_template('notAuthent.html')
        ans = ""
        context = RequestContext(request, {'user' : user, 'message' : ans})
    return HttpResponse(template.render (context))


def insertcontent(request):
    if request.user.is_authenticated():
        if request.method == "PUT" or request.method == "POST":
            info = request.body
            try:
                split_list = info.split('&', 2)
                name = split_list[1].split('=')[1]
                content = split_list[2].split('=')[1]
            except IndexError:
                ans = "Bad input: name=content"
                return HttpResponse(ans)
            page = Pages(name=name, page=content)
            page.save()
            ans = "Todo ha ido ok"
            user = request.user.username
            template = get_template("authent.html")
        else:
            return HttpResponseNotAllowed("Method Not Allowed")
    else:
        user = ""
        template = get_template('notAuthent.html')
        ans = ""
    context = RequestContext(request, {'user' : user, 'message' : ans})
    return HttpResponse(template.render(context))