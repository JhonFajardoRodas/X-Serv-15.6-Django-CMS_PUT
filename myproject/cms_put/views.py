from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import Pages
from django.views.decorators.csrf import csrf_exempt
 
# Create your views here.


@csrf_exempt
def processRequest(request, resource):
    if request.method == "GET":
        try:
            entry = Pages.objects.get(name=resource)
            return HttpResponse(entry.page)
        except Pages.DoesNotExist:
            return HttpResponseNotFound("Not found entry!")
    elif request.method == "POST":
        entryNew = Pages(name=resource, page=request.body)
        entryNew.save()
        return HttpResponse("Ok !")


