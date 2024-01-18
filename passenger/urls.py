from django.urls import path
from .views import PassengerRegistrationView, RegistrationConfirmationView, ActivateAccountView,PassengerloginView, ProfileUpdateView, PassengerLogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('register/', PassengerRegistrationView.as_view(), name='passenger_register'),
    path('confirm-message/', RegistrationConfirmationView.as_view(), name='confirm_register'),
    path('activate/<uid64>/<token>/', ActivateAccountView.as_view(), name='activate_account'),
    path('login/', PassengerloginView.as_view(), name='passenger_login'),
    path('logout/', PassengerLogoutView, name='passenger_logout'),
    path('profile/', ProfileUpdateView.as_view(), name='passenger_profile'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(),
         name='password_change_done'),
]
