from django.urls import path
from .views import TrainReviewView, ContactUsView

urlpatterns = [
    path('train/<int:train_id>/', TrainReviewView.as_view(), name='train_review'),
    path('contact-us/', ContactUsView.as_view(), name='contact_us'),
]
