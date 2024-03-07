from django.db import models

# Create your models here.
class Categoria(models.Model):
     nombre=models.CharField(max_length=50)

class Vendedor(models.Model):
     documento=models.BigIntegerField()
     nombre=models.CharField(max_length=50)
     apellido=models.CharField(max_length=50)
     direccion=models.CharField(max_length=50)
     correo=models.EmailField(max_length=50)
     telefono=models.CharField(max_length=50)
     
     
class Vehiculo(models.Model):
     categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
     vendedor=models.ForeignKey(Vendedor,on_delete=models.CASCADE)
     placa=models.CharField(max_length=6,primary_key=True)
     modelo=models.IntegerField()
     color=models.CharField(max_length=20)
     estado=models.CharField(max_length=20)
     precio=models.IntegerField()
     
     