
# Create your views here.
from django.shortcuts import render
from App1.models import Curso, Profesor, Estudiante
from django.http import HttpResponse
from App1.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario 
from django.contrib.auth.decorators import login_required


# Create your views here.
def inicio(request):
    return render(request, 'App1/inicio.html')
@login_required
def cursos(request):
    return render(request,'App1/cursos.html')
@login_required
def profesores(request):
    return render(request,'App1/profesores.html')
@login_required
def estudiantes(request):
    return render(request,'App1/estudiantes.html')


def busquedaCurso(request):
     return render(request,'App1/busquedaCurso.html')

def buscar(request):
     if request.GET['curso']:
          curso = request.GET['curso']
          cursos= Curso.objects.filter(curso__icontains=curso)

          return render(request,'App1/inicio.html', {"cursos":cursos, "comisiones": curso })
     else:
          respuesta= "No enviaste datos"

     #return HttpResponse(respuesta)
     return render(request,"App1/inicio.html",{"respuesta":respuesta})

#------CRUD ----------#
#----Cursos
def leerCursos(request):
    cursos= Curso.objects.all() 
    contexto= {"cursos": cursos}
    return render(request, "App1/leerCursos.html",contexto)

def cursos(request):
    if request.method =='POST':
        miFormulario=CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            curso=Curso(int(informacion['id']),str(informacion['nombre']),int(informacion['curso']))
            curso.save()
            return render(request, 'App1/inicio.html')
    else:
        miFormulario=CursoFormulario()
    return render(request, 'App1/cursos.html', {"miFormulario": miFormulario})

def eliminarCurso(request, curso_nombre):
    curso = Curso.objects.get(nombre=curso_nombre)
    curso.delete()
    # vuelvo al menú
    cursos = Curso.objects.all()  # trae todos los cursos
    contexto = {"cursos": cursos}
    return render(request, "App1/leerCursos.html", contexto)

def editarCurso(request, curso_nombre):
    # Recibe el nombre del curso que vamos a modificar
    curso = Curso.objects.get(nombre=curso_nombre)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data

            curso.nombre = informacion['nombre']
            curso.curso = informacion['curso']
            curso.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "App1/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = CursoFormulario(initial={'nombre': curso.nombre, 'curso': curso.curso})
    # Voy al html que me permite editar
    return render(request, "App1/editarCurso.html", {"miFormulario": miFormulario, "curso_nombre": curso_nombre})


#----Profesores
def leerProfesores(request):
    profesores= Profesor.objects.all() 
    contexto= {"profesores": profesores}
    return render(request, "App1/leerProfesores.html",contexto)

def profesores(request):
    if request.method =='POST':
        miFormulario=ProfesorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Profesor(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),
                                   informacion['email'], informacion['profesion'])
            curso.save()
            return render(request, "App1/inicio.html")
    else:
        miFormulario=ProfesorFormulario()
    return render(request, 'App1/profesores.html', {"miFormulario": miFormulario})

def eliminarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
    # vuelvo al menú
    profesores = Profesor.objects.all()  # trae todos los profesores 
    contexto = {"profesores": profesores}
    return render(request, "App1/leerProfesores.html", contexto)

def editarProfesor(request, profesor_nombre):
    # Recibe el nombre del profesor que vamos a modificar
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']
            profesor.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "App1/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido,
                                                   'email': profesor.email, 'profesion': profesor.profesion})
    # Voy al html que me permite editar
    return render(request, "App1/editarProfesor.html", {"miFormulario": miFormulario, "profesor_nombre": profesor_nombre})

#----Estudiantes
def leerEstudiantes(request):
    estudiantes= Estudiante.objects.all() # trae a todos los estudiantes
    contexto= {"estudiantes": estudiantes}
    return render(request, "App1/leerEstudiantes.html",contexto)

def estudiantes(request):
    if request.method =='POST':
        miFormulario=EstudianteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Estudiante(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),
                                   informacion['email'])
            curso.save()
            return render(request, "App1/inicio.html")
    else:
        miFormulario=EstudianteFormulario()
    return render(request, 'App1/estudiantes.html', {"miFormulario": miFormulario})

def eliminarEstudiante(request, estudiante_nombre):
    estudiante = Estudiante.objects.get(nombre=estudiante_nombre)
    estudiante.delete()
    # vuelvo al menú
    estudiantes = Estudiante.objects.all()  # trae todos los profesores 
    contexto = {"estudiantes": estudiantes}
    return render(request, "App1/leerEstudiantes.html", contexto)

def editarEstudiante(request, estudiante_nombre):
    # Recibe el nombre del estudiante que vamos a modificar
    estudiante = Estudiante.objects.get(nombre=estudiante_nombre)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = EstudianteFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data

            estudiante.nombre = informacion['nombre']
            estudiante.apellido = informacion['apellido']
            estudiante.email = informacion['email']
            estudiante.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "App1/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = EstudianteFormulario(initial={'nombre': estudiante.nombre, 'apellido': estudiante.apellido,
                                                   'email': estudiante.email})
    # Voy al html que me permite editar
    return render(request, "App1/editarEstudiantes.html", {"miFormulario": miFormulario, "estudiante_nombre": estudiante_nombre})


#------Login - Register ---------#      
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login,logout,authenticate   
from App1.forms import UserRegisterForm

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return render(request, "App1/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "App1/inicio.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "App1/inicio.html", {"mensaje":"Este formulario no es correcto"})
    form = AuthenticationForm()
    return render(request, "App1/login.html", {"form": form})


def register(request):
      if request.method == 'POST':
            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"App1/inicio.html" ,  {"mensaje":"Usuario creado correctamente!"})
      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     
      return render(request,"App1/registro.html" ,  {"form":form})

#------Editar Perfil-----#
from App1.forms import UserRegisterForm,UserEditForm

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
            return render(request, "App1/inicio.html")
    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})
    return render(request, "App1/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

#----------Avatar-------#
from App1.models import Avatar

def some_view(request):
    user_avatar = Avatar.objects.get(user=request.user)
    return render(request, 'padre.html', {'user_avatar': user_avatar})

from django.contrib.auth.models import User
from .forms import AvatarFormulario

@login_required
def agregarAvatar(request):
      if request.method == 'POST':
            miFormulario = AvatarFormulario(request.POST, request.FILES) #aquí mellega toda la información del html
            if miFormulario.is_valid():   #Si pasó la validación de Django
                  u = User.objects.get(username=request.user)
                  avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen']) 
                  avatar.save()
                  return render(request, "App1/inicio.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= AvatarFormulario() #Formulario vacio para construir el html
      return render(request, "App1/agregarAvatar.html", {"miFormulario":miFormulario})