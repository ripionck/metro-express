from django.urls import path
from .views import TrainCreateView, TrainUpdateView, TrainDeleteView, ScheduleCreateView, ScheduleListView, ScheduleUpdateView, ScheduleDeleteView, TrainListView, TrainReviewView, ScheduleView, TrainInformationSearchView

urlpatterns = [
    path('create/', TrainCreateView.as_view(), name='train_create'),
    path('update/<int:pk>', TrainUpdateView.as_view(), name='train_update'),
    path('delete/<int:pk>/', TrainDeleteView.as_view(), name='train_delete'),
    path('schedule/create/', ScheduleCreateView.as_view(), name='schedule_create'),
    path('schedule-list/', ScheduleListView.as_view(), name='schedule_list'),
    path('schedule/<int:pk>/update/', ScheduleUpdateView.as_view(), name='schedule_update'),
    path('schedule/<int:pk>/delete/', ScheduleDeleteView.as_view(), name='schedule_delete'),
    path('schedule/<int:train_id>/', ScheduleView.as_view(), name='schedule_view'),
    path('train-information_search/', TrainInformationSearchView.as_view(), name='train_information_search'),
    path('train/<int:train_id>/', TrainReviewView.as_view(), name='train_review'),
]
