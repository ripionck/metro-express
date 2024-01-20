from django.urls import path
from .views import BookingListView, BookTrainView

urlpatterns = [
    path('booking_list/', BookingListView.as_view(), name='booking_list'),
    path('book-train/<int:train_id>/', BookTrainView.as_view(), name='book_train'),
]
