from django.shortcuts import render


def bag(request):
    """ Bag view """
    
    return render(request, 'bag/bag.html')
