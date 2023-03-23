from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *


def cursos(request):

    if request.method == "POST":
        mi_form = CursoForm(request.POST)
        if mi_form.is_valid():
            informacion = mi_form.cleaned_data
            curso_save = Curso(
                nombre=informacion['nombre'],
                camada=informacion['camada']
            )
            curso_save.save()
    all_cursos = Curso.objects.all()
    context = {
        "cursos": all_cursos,
        "form": CursoForm(),
        "form_busqueda": BusquedaCursoForm(),
    }
    return render(request, "AppCoder/cursos.html", context=context)

def inicio(request):
    return render(request, "index.html")
def estudiantes(request):

    if request.method == "POST":
        mi_formulario = EstudiantesForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            estudiante_save = Estudiantes(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                email=informacion['email']
            )
            estudiante_save.save()
    all_students = Estudiantes.objects.all()
    context1 = {
        "nombre": all_students,
        "apellido": all_students,
        "form": EstudiantesForm(),
        "form_busqueda": BusquedaEstudianteForm(),
    }
    return render(request, "AppCoder/estudiantes.html", context=context1)

def profesores(request):
    return render(request, "index.html")

def crear_curso(request, nombre, camada):
    save_curso = Curso(nombre = nombre, camada= int(camada))
    save_curso.save()
    context = {
            "nombre": nombre
    }
    return render(request, "AppCoder/save_curso.html", context)

def busqueda_curso(request):
    #MOSTRAR DATOS FILTRADOS#
    mi_form = BusquedaCursoForm(request.GET)
    if mi_form.is_valid():
        informacion = mi_form.cleaned_data
        cursos_filtrados = Curso.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "cursos": cursos_filtrados
        }

    return render(request, "AppCoder/busqueda_curso.html", context= context)

def busqueda_estudiante(request):
    #MOSTRAR DATOS FILTRADOS#
    mi_formulario1 = BusquedaEstudianteForm(request.GET)
    if mi_formulario1.is_valid():
        informacion1 = mi_formulario1.cleaned_data
        students_filtrados = Estudiantes.objects.filter(nombre__icontains=informacion1['nombre'],
                                                        apellido__icontains=informacion1['apellido'])
        context1 = {
            "estudiante": students_filtrados
        }

    return render(request, "AppCoder/busqueda_estudiantes.html", context= context1)
