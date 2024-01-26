from django.urls import path
from .views import  HomeView, ContactUsView

urlpatterns = [
    path('contact-us/', ContactUsView.as_view(), name='contact_us'),
    path('search/', HomeView.as_view(), name='train_search'),
]
