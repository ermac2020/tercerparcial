from django.db import models
from django.contrib import admin
from django.utils import timezone

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits = 8, decimal_places = 2)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=180)
    telefono = models.CharField(max_length=8)
    direccion = models.CharField(max_length=100)
    estado = models.CharField(max_length=12, blank=True, null=True)
    cursos = models.ManyToManyField(Curso, through='Inscribir')

    def completar(self):
        self.estado = "Completo"
        self.save

    def __str__(self):
        return self.nombre

class Inscribir(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

class InscribirInLine(admin.TabularInline):
    model = Inscribir
    extra = 1

class CursoAdmin(admin.ModelAdmin):
    inlines = (InscribirInLine,)

class EstudianteAdmin(admin.ModelAdmin):
    inlines = (InscribirInLine,)
