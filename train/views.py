from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Train, Station, Schedule, TrainReview
from .forms import TrainSearchForm



# Create your views here.
class TrainListView(View):
    template_name = 'trains/trains_list.html'

    def get(self, request):
        trains = Train.objects.all()
        return render(request, self.template_name, {'trains': trains})
    
class ScheduleView(View):
    template_name = 'trains/schedule.html'

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
            return render(self.request, 'trains/search_results.html', context)
        except Station.DoesNotExist:
            return render(self.request, 'trains/not_found.html')  
   
class NotFoundView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'not_found.html')
    
class TrainReviewView(LoginRequiredMixin, View):
    template_name = 'trains/train_review.html'

    def get(self, request, train_id):
        train = get_object_or_404(Train, id=train_id)
        reviews = TrainReview.objects.filter(train=train)
        return render(request, self.template_name, {'train': train, 'reviews': reviews})

    def post(self, request, train_id):
        train = get_object_or_404(Train, id=train_id)
        comment = request.POST.get('comment')
        user_review = TrainReview(train=train, user=request.user, comment=comment)
        user_review.save()
        return HttpResponseRedirect(reverse('train_review', args=[train_id]))