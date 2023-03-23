
from django.contrib import admin
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('inicio/', inicio, name="AppCoderInicio"),
    path('registro_o_loggin/', cursos, name="AppCoderCursos"),
    path('buscar_curso/', busqueda_curso, name="AppCoderBuscarCursos"),
    path('estudiantes/', estudiantes, name="AppCoderEstudiantes"),
    path('buscar_estudiantes/', busqueda_estudiante, name="AppCoderBuscarEstudiantes"),
    path('profesores/', profesores, name="AppCoderProfesores"),
    path('registro/<nombre>/<camada>', crear_curso, name="AppCoderCurso"),

]

