from django.urls import path 
from . import views

urlpatterns = [
    path('', views.produtoIndex)
]

#caminho = /produto