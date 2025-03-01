from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def hola_mundo(request):
    return render(request,'holamundo.html')

# Vista basada en clase
class adios_mundo(TemplateView):
    template_name = 'adios.html'

