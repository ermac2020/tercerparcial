from django import forms
from .models import Estudiante, Curso

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ('nombre', 'telefono', 'direccion', 'cursos')

    def __init__ (self, *args, **kwargs):
        super(EstudianteForm, self).__init__(*args, **kwargs)
        self.fields["cursos"].help_text = "Seleccione materias a cursar"
        self.fields["cursos"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["cursos"].queryset = Curso.objects.all()
