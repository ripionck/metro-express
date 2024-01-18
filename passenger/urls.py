from django.urls import path
from .views import PassengerRegistrationView

urlpatterns = [
    path('register/', PassengerRegistrationView.as_view(), name='passenger_register')
]
