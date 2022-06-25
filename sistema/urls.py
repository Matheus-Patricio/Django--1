from django.urls import path
from . import views

urlpatterns = [
    path('sistema/', views.sistemaIndex)
]

# caminho = sistema/sistema