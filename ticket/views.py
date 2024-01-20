from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from .models import Ticket
from train.models import Train
from .forms import TicketForm


# Create your views here
class BookingListView(LoginRequiredMixin, View):
    template_name = 'booking_list.html'

    def get(self, request, *args, **kwargs):
        user_bookings = Ticket.objects.filter(user=request.user)
        print(user_bookings)
        return render(request, self.template_name, {'user_bookings': user_bookings})


class BookTrainView(FormView):
    template_name = 'book_train.html'
    form_class = TicketForm

    def form_valid(self, form):
        user = self.request.user
        train_id = self.kwargs['train_id']
        train = get_object_or_404(Train, id=train_id)

        seat_count = form.cleaned_data['seats_booked']
        selected_seat = form.cleaned_data['selected_seat']
        class_type = form.cleaned_data['class_type']
        from_station = form.cleaned_data['from_station']
        to_station = form.cleaned_data['to_station']

        # Check if there are enough available seats
        if train.available_seats >= seat_count:
            # Create a booking
            Ticket.objects.create(user=user, train=train, seats_booked=seat_count,
                                             selected_seat=selected_seat, class_type=class_type,from_station=from_station,to_station=to_station)
            
            # Update available seats on the train
            train.available_seats -= seat_count
            train.save()

            return redirect('booking_list')
        else:
            form.add_error('seat_count', 'Not enough available seats.')
            return self.form_invalid(form)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})