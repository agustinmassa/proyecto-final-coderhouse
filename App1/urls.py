from django.urls import path
from App1 import views
from django.contrib.auth.views import LogoutView 
from django.contrib.auth.decorators import login_required

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), 
    path('cursos', login_required(views.cursos), name="Cursos"),
    path('profesores', login_required(views.profesores), name="Profesores"),
    path('estudiantes', login_required(views.estudiantes), name="Estudiantes"),
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    #path('estudianteFormulario', views.estudianteFormulario, name="EstudianteFormulario"),
    #path('busquedaCurso',views.busquedaCurso,name="BusquedaCurso"),
    #path('buscar/',views.buscar),
    #------CRUD----------#
    #------Cursos----------#
    path('leerCursos',login_required(views.leerCursos),name='Cursos'),
    path('cursoFormulario', views.cursos, name="CursoFormulario"),
    path('eliminarCurso/<curso_nombre>/', views.eliminarCurso, name="EliminarCurso"), 
    path('editarCurso/<curso_nombre>/', views.editarCurso, name="EditarCurso"),
    #------Profesores----------#
    path('leerProfesores',login_required(views.leerProfesores),name='Profesores'),
    path('profesorFormulario', views.profesores, name="ProfesorFormulario"),
    path('eliminarProfesor/<profesor_nombre>/', views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>/', views.editarProfesor, name="EditarProfesor"),
    #------Estudiantes----------#
    path('leerEstudiantes',login_required(views.leerEstudiantes),name='Estudiantes'),
    path('estudianteFormulario', views.estudiantes, name="EstudianteFormulario"),
    path('eliminarEstudiante/<estudiante_nombre>/', views.eliminarEstudiante, name="EliminarEstudiante"),
    path('editarEstudiante/<estudiante_nombre>/', views.editarEstudiante, name="EditarEstudiante"),
    #------Login-Register-Logout----------#
    path('login',views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='App1/logout.html'), name='Logout'), 
    #------Edit de perfil-----#
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    #------Agregar Avatar-----#
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
]

