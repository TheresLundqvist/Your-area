from django.shortcuts import render

# Create your views here.


def about(request):
    """ View to return about page """

    return render(request, 'about/about.html')
