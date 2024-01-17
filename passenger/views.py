from django.shortcuts import render, redirect
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from .models import Passenger
from .forms import PassengerCreationForm

# Create your views here.
class PassengerView(View):
    template_name = 'passenger_list.html'

    def get(self, request):
        passengers = Passenger.objects.all()
        return render(request, self.template_name, {'passengers': passengers})

    def post(self, request):
        # Assuming you have a PassengerForm for validation
        form = PassengerCreationForm(request.POST)

        if form.is_valid():
            # Create a new Passenger instance
            new_passenger = form.save()
            
            # Optionally, perform additional actions or validations
            
            return JsonResponse({'success': True, 'message': 'Passenger created successfully'})
        else:
            # If the form is not valid, return error messages
            return JsonResponse({'success': False, 'errors': form.errors})

class UserRegistrationView(View):
    template_name = 'registration_form.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_active = False
        user.save()

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        confirm_link = f'http://{request.get_host()}{reverse("activate", args=[uid, token])}'

        email_subject = 'Confirm Your Email'
        email_body = render_to_string('confirm_email.html', {'confirm_link': confirm_link})
        email = EmailMultiAlternatives(email_subject, '', to=[user.email])
        email.attach_alternative(email_body, 'text/html')
        email.send()

        return HttpResponse('Check your email for confirmation')

class ActivationView(View):
    def get(self, request, uid64, token):
        try:
            uid = urlsafe_base64_decode(uid64).decode()
            user = User._default_manager.get(pk=uid)
        except User.DoesNotExist:
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('login')
        else:
            return HttpResponse('Activation link is invalid!')

class UserLoginView(View):
    template_name = 'login_form.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, self.template_name, {'error': 'Invalid Credential!'})

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class UserEditView(View):
    template_name = 'edit_user.html'

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        return render(request, self.template_name, {'user': user})

    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect('dashboard')  # Change 'dashboard' to the desired URL after editing the user
