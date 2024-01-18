from django.urls import path
from .views import PassengerRegistrationView,PassengerloginView

urlpatterns = [
    path('register/', PassengerRegistrationView.as_view(), name='passenger_register'),
    path('login/', PassengerloginView.as_view(), name='passenger_login')
]
