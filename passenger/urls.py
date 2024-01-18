from django.urls import path
from .views import PassengerRegistrationView,PassengerloginView, ProfileUpdateView, PassengerLogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('register/', PassengerRegistrationView.as_view(), name='passenger_register'),
    path('login/', PassengerloginView.as_view(), name='passenger_login'),
    path('logout/', PassengerLogoutView.as_view(), name='passenger_logout'),
    path('profile/', ProfileUpdateView.as_view(), name='passenger_profile'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(),
         name='password_change_done'),
]
