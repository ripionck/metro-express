from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Train, Station, Schedule, TrainReview
from .forms import TrainForm, TrainUpdateForm, TrainSearchForm, ScheduleForm, ScheduleUpdateForm


# Create your views here.
class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

class TrainCreateView(AdminRequiredMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'train/train_create.html'
    success_url = reverse_lazy('train_list')

class TrainUpdateView(AdminRequiredMixin, UpdateView):
    model = Train
    form_class = TrainUpdateForm
    success_url = reverse_lazy('train_list')
    template_name = 'train/train_update.html'

class TrainDeleteView(AdminRequiredMixin, DeleteView):
    model = Train
    success_url = reverse_lazy('train_list') 

class ScheduleCreateView(AdminRequiredMixin, CreateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = 'schedule/schedule_create.html'
    success_url = reverse_lazy('schedule_list')

class ScheduleUpdateView(AdminRequiredMixin, UpdateView):
    model = Schedule
    form_class = ScheduleUpdateForm
    template_name = 'schedule/schedule_update.html'
    success_url = reverse_lazy('schedule_list')

class ScheduleDeleteView(AdminRequiredMixin, DeleteView):
    model = Schedule
    success_url = reverse_lazy('schedule_list')  

class TrainListView(View):
    template_name = 'train/trains_list.html'

    def get(self, request):
        trains = Train.objects.all()
        return render(request, self.template_name, {'trains': trains})
    
class ScheduleListView(View):
    template_name = 'schedule/schedule_list.html'

    def get(self, request):
        schedules= Schedule.objects.all()
        return render(request, self.template_name, {'schedules': schedules})
    
class ScheduleView(View):
    template_name = 'schedule/schedule_view.html'

    def get(self, request, train_id):
        schedule = Schedule.objects.filter(train_id=train_id)
        return render(request, self.template_name, {'schedule': schedule})

class TrainSearchView(FormView):
    template_name = 'index.html'
    form_class = TrainSearchForm

    def form_valid(self, form):
        from_station_name = form.cleaned_data['from_station']
        to_station_name = form.cleaned_data['to_station']
        date = form.cleaned_data['date']
        travel_class = form.cleaned_data['travel_class']

        try:
            # Get the related stations using their names
            from_station = Station.objects.get(name__iexact=from_station_name)
            to_station = Station.objects.get(name__iexact=to_station_name)

            # Filter the queryset based on the form data
            search_results = Train.objects.filter(
                start_station__exact=from_station,
                end_station__exact=to_station,
            )

            context = {'search_results': search_results}
            return render(self.request, 'train/search_results.html', context)
        except Station.DoesNotExist:
            return render(self.request, 'train/not_found.html')  
   
class NotFoundView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'not_found.html')
    
class TrainReviewView(LoginRequiredMixin, View):
    template_name = 'train/train_review.html'

    def get(self, request, train_id):
        train = get_object_or_404(Train, id=train_id)
        reviews = TrainReview.objects.filter(train=train)
        return render(request, self.template_name, {'train': train, 'reviews': reviews})

    def post(self, request, train_id):
        train = get_object_or_404(Train, id=train_id)
        comment = request.POST.get('comment')
        user_review = TrainReview(train=train, user=request.user.passenger_profile, comment=comment)
        user_review.save()
        return HttpResponseRedirect(reverse('train_review', args=[train_id]))