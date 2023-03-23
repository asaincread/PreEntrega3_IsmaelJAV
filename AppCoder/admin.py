from django.contrib import admin
from AppCoder.models import Curso, Estudiantes, Profesor, Entregable

# Register your models here.
admin.site.register(Curso)
admin.site.register(Estudiantes)
admin.site.register(Profesor)
admin.site.register(Entregable)