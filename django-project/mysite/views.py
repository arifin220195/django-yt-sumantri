from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render (request, 'index.html')
def blog(request):
    return HttpResponse('Ini adalah halaman blog')

