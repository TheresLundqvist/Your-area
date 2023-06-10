from django.shortcuts import render

# Create your views here.


def gallery(request):
    """ View to return gallery page """

    return render(request, 'gallery/gallery.html')
