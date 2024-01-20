from django.urls import path
from .views import TrainCreateView, TrainUpdateView, TrainDeleteView, ScheduleCreateView, ScheduleListView, ScheduleUpdateView, ScheduleDeleteView, TrainListView, TrainSearchView, NotFoundView, TrainReviewView, ScheduleView



urlpatterns = [
    path('create/', TrainCreateView.as_view(), name='train_create'),
    path('train-list/', TrainListView.as_view(), name='train_list'),
    path('update/<int:pk>', TrainUpdateView.as_view(), name='train_update'),
    path('delete/<int:pk>/', TrainDeleteView.as_view(), name='train_delete'),
    path('schedule/create/', ScheduleCreateView.as_view(), name='schedule_create'),
    path('schedule-list/', ScheduleListView.as_view(), name='schedule_list'),
    path('schedule/<int:pk>/update/', ScheduleUpdateView.as_view(), name='schedule_update'),
    path('schedule/<int:pk>/delete/', ScheduleDeleteView.as_view(), name='schedule_delete'),
    path('schedule/<int:train_id>/', ScheduleView.as_view(), name='schedule_view'),
    path('search-train/', TrainSearchView.as_view(), name='search_train'),
    path('not-found/', NotFoundView.as_view(), name='not_found'),
    path('train/<int:train_id>/', TrainReviewView.as_view(), name='train_review'),
]
