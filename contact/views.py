from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .forms import ContactForm


def contact(request):
    """ Contact view """
    def _send_contact_email(self, form):
        contact_email = form.email
        subject = render_to_string(
            'contact/contact_emails/email_subject.txt',
            {'form': form,})
        message = render_to_string(
        'contact/contact_emails/email_message.txt',
        { 'form': form, 'reciever': settings.DEFAULT_TO_EMAIL})
    
        send_mail(
            
            subject,
            message,
            contact_email,
            [settings.DEFAULT_TO_EMAIL]
        )
    
    if request.method == 'POST':
        form = ContactForm(request.POST)        

        if form.is_valid():            
            self._send_contact_email(form)
            messages.success(request, "Message sent!")
            return redirect(request, 'home')
        else:
            messages.error(request, "Sorry, your form can't be processed at the moment.\
                            Please check and try again.")
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
