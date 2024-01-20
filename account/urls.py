from django.urls import path
from .views import PassengerRegistrationView, RegistrationConfirmationView, activate,PassengerloginView, ProfileUpdateView, PassengerLogoutView, PasswordChangeView

urlpatterns = [
    path('register/', PassengerRegistrationView.as_view(), name='passenger_register'),
    path('confirm-message/', RegistrationConfirmationView.as_view(), name='confirm_register'),
    path('active/<uid64>/<token>/', activate, name='activate'),
    path('login/', PassengerloginView.as_view(), name='passenger_login'),
    path('logout/', PassengerLogoutView, name='passenger_logout'),
    path('profile/', ProfileUpdateView.as_view(), name='passenger_profile'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
]
