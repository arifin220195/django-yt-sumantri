from django.http import HttpResponse


def index(request):
    return HttpResponse('Halo Everyone')
def blog(request):
    return HttpResponse('Ini adalah halaman blog')

