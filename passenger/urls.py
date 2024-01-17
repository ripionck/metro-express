from django.urls import path
from .views import PassengerView

urlpatterns = [
    path('register/', PassengerView.as_view(), name='passenger_register')
]
