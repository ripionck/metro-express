from django.urls import path
from .views import TrainListView

urlpatterns = [
    path('train-list/', TrainListView.as_view(), name='trains')
]
