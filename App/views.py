from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Dhi(request):
    return HttpResponse('<marquee><h1>Dhiraj Goud</h1></marquee>')

def DG(request):
    return HttpResponse('<marquee><b>DG</b></marquee>')