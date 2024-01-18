from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .forms import PassengerRegistrationForm, ProfileUpdateForm

# Create your views here.

class PassengerRegistrationView(FormView):
    template_name = 'passengers/passenger_register.html'
    form_class = PassengerRegistrationForm
    success_url = reverse_lazy('passenger_register')

    def form_valid(self, form):
        print(form.cleaned_data)
        # Save the user instance and log in the user
        user = form.save()
        login(self.request, user)
        # Redirect to the success URL (user's profile page)
        return super().form_valid(form)
    
class PassengerloginView(LoginView):
    template_name = 'passengers/passenger_login.html'

    def get_success_url(self):
        return reverse_lazy('home')
    
class ProfileUpdateView(View):
    template_name = 'passengers/passenger_profile.html'

    def get(self, request):
        # Retrieve the UserUpdateForm instance with the user's data
        form = ProfileUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # Process the form submission with user data in POST
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('passenger_profile')
        
        return render(request, self.template_name, {'form': form})