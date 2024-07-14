from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to="categorias", null=True)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    marca = models.CharField(max_length=150)
    nombre = models.CharField(max_length=300)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    precio_oferta = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
    

class Bicicleta(Producto):
    image = models.ImageField(upload_to='bicicletas')


    class Meta:
        verbose_name = 'bicicleta'
        verbose_name_plural = 'bicicletas'

class Neumatico(Producto):
    image = models.ImageField(upload_to='neumaticos')

    class Meta:
        verbose_name = 'neumático'
        verbose_name_plural = 'neumáticos'

class Freno(Producto):
    image = models.ImageField(upload_to='frenos')

    class Meta:
        verbose_name = 'freno'
        verbose_name_plural = 'frenos'
