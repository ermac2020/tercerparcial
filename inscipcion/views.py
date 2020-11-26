from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import EstudianteForm
from inscipcion.models import Estudiante, Inscribir

def principal(request):
    return render(request, 'inscripcion/principal.html')

def inscripcion_nuevo(request):
    if request.method == "POST":
        formulario = EstudianteForm(request.POST)
        if formulario.is_valid():
            estudiante = Estudiante.objects.create(nombre=formulario.cleaned_data['nombre'], telefono=formulario.cleaned_data['telefono'], direccion=formulario.cleaned_data['direccion'])
            for curso_id in request.POST.getlist('cursos'):
                inscribir = Inscribir(curso_id=curso_id, estudiante_id=estudiante.id)
                inscribir.save()
            messages.add_message(request, messages.SUCCESS, 'Estudiante Guardado')
            formulario = EstudianteForm()
    else:
        formulario = EstudianteForm()
    return render(request, 'inscripcion/inscripcion_nuevo.html', {'formulario':formulario})

def inscripcion_lista(request):
    estudiantes = Estudiante.objects.filter()
    return render(request, 'inscripcion/inscripcion_lista.html', {'estudiantes': estudiantes})

def inscripcion_detalle(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    cursos = estudiante.cursos.all()
    total = 0
    for curso in cursos:
        total = total + curso.costo
    return render(request, 'inscripcion/inscripcion_detalle.html', {'estudiante':estudiante, 'cursos':cursos, 'total':total})
