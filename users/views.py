from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import render, redirect


def login(request):
    """
    Presenta el formulario de login y gestiona el login de un usuario
    :param request: objeto HttpRequest con los datos de la petición
    :return: HttpResponse con la plantilla
    """
    error_message = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        user = authenticate(username=username, password=password)
        if user is None:
            error_message = "Nombre de usuario o contraseña incorrecto"
        else:
            if user.is_active:
                django_login(request, user)
                return redirect("/")
            else:
                error_message = "Cuenta de usuario inactiva"

    return render(request, 'users/login.html', {'error': error_message})


def logout(request):
    """
    Hace el logout de un usuario y redirige al login
    :param request: objeto HttpRequest con los datos de la petición
    :return: HttpResponse con la plantilla
    """
    if request.user.is_authenticated():
        django_logout(request)
    return redirect("/")