from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView

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

        # Here, you can add your logic to handle the form data
        # For example, you can send an email, save to the database, etc.

        return HttpResponseRedirect(reverse('contact_us'))

