import datetime
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    now = datetime.datetime.now()
    html = "<html><body><h2>Now the time is %s.</h2></body></html>"%now
    return HttpResponse(html)
# def welcome(request):
#     return HttpResponse("Welcome to the django class")
# def intro(request):
#     return HttpResponse("Just then, the king felt true fear for the first time")
def pageone(request):
    return render(request, 'index.html')