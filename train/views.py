from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Train, Station, Schedule, TrainReview
from .forms import TrainForm, TrainUpdateForm,  ScheduleForm, ScheduleUpdateForm


# Create your views here.
class TrainInformationSearchView(View):
    template_name = 'train/train_information_search.html'

    def get(self, request, *args, **kwargs):
        trains = Train.objects.all()
        return render(request, self.template_name, {'trains': trains})

    def post(self, request, *args, **kwargs):
        train_name = request.POST.get('train_name')

        try:
            train = Train.objects.get(name=train_name)
            reviews = TrainReview.objects.filter(train=train)
            schedules = Schedule.objects.filter(train=train).select_related('station')
            search_result = {'train': train, 'reviews': reviews, 'schedules':schedules}
        except Train.DoesNotExist:
            search_result = None

        trains = Train.objects.all()

        return render(request, self.template_name, {'search_result': search_result, 'trains':trains, 'selected_train': train_name})

    
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
    template_name = 'train/train_list.html'

    def get(self, request):
        trains = Train.objects.all()
        return render(request, self.template_name, {'trains': trains})
    
class ScheduleListView(View):
    template_name = 'schedule/schedule_list.html'

    def get(self, request):
        schedules= Schedule.objects.all()
        return render(request, self.template_name, {'schedules': schedules})
    
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