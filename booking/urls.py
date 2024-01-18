from django.urls import path
from .views import BookingListView

urlpatterns = [
    
    path('booking_list/', BookingListView.as_view(), name='booking_list'),
]
