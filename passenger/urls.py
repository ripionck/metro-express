from django.urls import path
from .views import PassengerRegistrationView,PassengerloginView, ProfileUpdateView, PassengerLogoutView

urlpatterns = [
    path('register/', PassengerRegistrationView.as_view(), name='passenger_register'),
    path('login/', PassengerloginView.as_view(), name='passenger_login'),
    path('logout/', PassengerLogoutView.as_view(), name='passenger_logout'),
    path('profile/', ProfileUpdateView.as_view(), name='passenger_profile')
]
