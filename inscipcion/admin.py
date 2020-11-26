from django.contrib import admin
from inscipcion.models import Curso, CursoAdmin, Estudiante, EstudianteAdmin

admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
