from django.shortcuts import render
""" Views for the about app """


def about(request):
    """ About view """
    return render(request, 'about/about.html')
