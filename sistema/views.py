from django.shortcuts import render

# Create your views here.

def sistemaIndex(request):
    return render(request, 'sistema/bipbup.html')