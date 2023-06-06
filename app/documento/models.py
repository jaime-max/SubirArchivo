from django.db import models

# Create your models here.
class ArchivoPDF(models.Model):
    archivo= models.FileField(upload_to='pdfs/')
    fecha_subida = models.DateTimeField(auto_now_add=True)