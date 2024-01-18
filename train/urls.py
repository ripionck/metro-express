from django.urls import path
from .views import TrainListView, TrainSearchView


urlpatterns = [
    path('train-list/', TrainListView.as_view(), name='trains'),
    path('search-train/', TrainSearchView.as_view(), name = 'search_train')
]
