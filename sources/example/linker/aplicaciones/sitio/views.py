from django.shortcuts import render

# Create your views here.


def indexView(request):
    return render(request, 'acceso.html')


def escritorioView(request):
    return render(request, 'escritorio.html')
