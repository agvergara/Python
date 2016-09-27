from django.shortcuts import render
from cms.models import Pages
from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def insertcontent(request):
    info = request.body
    try:
        name = info.split('=')[0]
        content = info.split('=')[1]
    except IndexError:
        ans = "Bad input: name=content"
        return HttpResponse(ans)
    if request.method == "PUT" or request.method == "POST":
        page = Pages(name=name, page=content)
        page.save()
        ans = "Todo ha ido ok"
    else:
        return HttpResponseNotAllowed("Method Not Allowed")
    return HttpResponse(ans)