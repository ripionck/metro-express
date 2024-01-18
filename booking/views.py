
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from .models import Booking
from train.models import Train
from .forms import BookingForm


# Create your views here
class BookingListView(LoginRequiredMixin, View):
    template_name = 'booking_list.html'

    def get(self, request, *args, **kwargs):
        user_bookings = Booking.objects.filter(user=request.user)
        print(user_bookings)
        return render(request, self.template_name, {'user_bookings': user_bookings})


class BookTrainView(FormView):
    template_name = 'book_train.html'
    form_class = BookingForm

    def form_valid(self, form):
        user = self.request.user
        train_id = self.kwargs['train_id']
        train = get_object_or_404(Train, id=train_id)

        seat_count = form.cleaned_data['seats_booked']
        selected_seat = form.cleaned_data['selected_seat']

        # Check if there are enough available seats
        if train.available_seats >= seat_count:
            # Create a booking
            booking = Booking.objects.create(user=user, train=train, seats_booked=seat_count,
                                             selected_seat=selected_seat)
            
            # Update available seats on the train
            train.available_seats -= seat_count
            train.save()

            # Redirect to a success page or display a success message
            return redirect('booking_list')
        else:
            # Display an error message if there are not enough available seats
            form.add_error('seat_count', 'Not enough available seats.')
            return self.form_invalid(form)

    def form_invalid(self, form):
        # Handle the case when the form is invalid
        return render(self.request, self.template_name, {'form': form})