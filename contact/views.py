from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm

def contact(request):

    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, "Message sent!")
            return redirect(request, 'home')
    else:
        form = ContactForm()
        messages.error(request, "Sorry, your form can't be processed at the moment.\
                        Please check and try again.")

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
