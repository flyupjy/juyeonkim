from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('contact:sent')
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            sender = form.cleaned_data.get('sender')
            subject = form.cleaned_data.get('subject')
            email_subject = f'"{subject}" from {sender}'
            message = form.cleaned_data.get('message')
            email_sender = settings.DEFAULT_FROM_EMAIL
            reciever = settings.ADMIN_EMAILS
            send_mail(email_subject, message, email_sender, reciever)

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    
class SentView(TemplateView):
    template_name = 'contact/sent.html'