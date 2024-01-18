from django.urls import path
from .views import PassengerRegistrationView,PassengerloginView, ProfileUpdateView

urlpatterns = [
    path('register/', PassengerRegistrationView.as_view(), name='passenger_register'),
    path('login/', PassengerloginView.as_view(), name='passenger_login'),
    path('profile/', ProfileUpdateView.as_view(), name='passenger_profile')
]
