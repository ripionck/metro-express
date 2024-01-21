from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView
from .models import ContactUs

# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

class ContactUsView(View):
    template_name = 'contact_us.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the form data to the database
        ContactUs.objects.create(name=name, email=email, message=message)
        messages.success(
            self.request,
            f'Your message sent successfully!'
        )

        # Optionally, can add logic to send an email or perform other actions here

        # Redirect to the contact_us page after the form is submitted
        return HttpResponseRedirect(reverse('contact_us'))


    