from django.shortcuts import render, redirect
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import FormView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, PasswordChangeView
from .forms import PassengerRegistrationForm, ProfileUpdateForm, PasswordChangeForm

# Create your views here.

class PassengerRegistrationView(FormView):
    template_name = 'passengers/passenger_register.html'
    form_class = PassengerRegistrationForm
    success_url = reverse_lazy('confirm_register')

    def form_valid(self, form):
        user = form.save()

        # Generate token and confirmation link
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        confirm_link = f'http://127.0.0.1:8000/passenger/activate/{uid}/{token}'

        # Send confirmation email
        email_subject = 'Confirm Your Email'
        email_body = render_to_string('passengers/confirm_email.html', {'confirm_link': confirm_link})
        email = EmailMultiAlternatives(email_subject, '', to=[user.email])
        email.attach_alternative(email_body, 'text/html')
        email.send()

        return redirect(self.success_url)

class RegistrationConfirmationView(View):
    template_name = 'passengers/confirm_message.html'

    def get_success_url(self):
        return reverse_lazy('confirm_register')


class ActivateAccountView(View):
    def get(self, request, uid64, token):
        try:
            uid = urlsafe_base64_decode(uid64).decode()
            user = User._default_manager.get(pk=uid)
        except User.DoesNotExist:
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('passenger_login')
        else:
            return redirect('passenger_register')

    
class PassengerloginView(LoginView):
    template_name = 'passengers/passenger_login.html'

    def get_success_url(self):
        return reverse_lazy('home')
    

def PassengerLogoutView(request):
    logout(request)
    return redirect('home')

    
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
    
class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'passengers/password_change.html'
    success_url = reverse_lazy('password_change_done')

class PasswordChangeDoneView(PasswordChangeView):
    template_name = 'passengers/password_change_done.html'
