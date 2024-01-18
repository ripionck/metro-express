
from django.shortcuts import render
from django.views import View
from .models import Booking
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here
class BookingListView(LoginRequiredMixin, View):
    template_name = 'booking_list.html'

    def get(self, request, *args, **kwargs):
        user_bookings = Booking.objects.filter(user=request.user)
        return render(request, self.template_name, {'user_bookings': user_bookings})
