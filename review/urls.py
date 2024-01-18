from django.urls import path
from .views import TrainReviewView

urlpatterns = [
    path('train/<int:train_id>/', TrainReviewView.as_view(), name='train_review'),
]
