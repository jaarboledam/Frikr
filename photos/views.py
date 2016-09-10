from django.shortcuts import render
from photos.models import Photo


def home(request):
    """
    Renderiza el home con un listado de fotos
    :param request: objeto HttpRequest
    :return: HttpResponse con la plantilla
    """
    photos = Photo.objects.all().order_by('-created_at')  # recupera todas las fotos de la base de datos ordenadas descendentemente (-)
    context = {'photos_list': photos[:4]}
    return render(request, 'photos/home.html', context)
