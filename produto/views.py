from django.shortcuts import render
# Create your views here.

def produtoIndex(request):
    return render(request, 'produto/index.html')