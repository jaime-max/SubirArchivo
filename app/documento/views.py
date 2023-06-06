from django.shortcuts import render

# Create your views here.
from .models import ArchivoPDF

def subir_archivo(request):
    if request.method == 'POST':
        archivo = request.FILES['archivo']
        ArchivoPDF.objects.create(archivo=archivo)
        return render(request,'doc/subir_archivo.html',{'mensaje':'archivo subido'})
    return  render(request, 'doc/subir_archivo.html')