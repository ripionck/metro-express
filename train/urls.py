from django.urls import path
from .views import TrainListView, TrainSearchView, NotFoundView, TrainReviewView, ScheduleView



urlpatterns = [
    path('train-list/', TrainListView.as_view(), name='trains'),
    path('schedule/<int:train_id>/', ScheduleView.as_view(), name='schedule_view'),
    path('search-train/', TrainSearchView.as_view(), name='search_train'),
    path('not-found/', NotFoundView.as_view(), name='not_found'),
    path('train/<int:train_id>/', TrainReviewView.as_view(), name='train_review'),
]
