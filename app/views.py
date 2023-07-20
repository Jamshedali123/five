from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jsp(request):
    return HttpResponse('<h1><marquee>Jspider python full stack developer</marquee></h1>')

def address(request):
    return HttpResponse('<h1><marquee>near klm mall marathahalli bridge</h1></marquee>')
