from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import FormView
from .models import Train, Station
from .forms import TrainSearchForm



# Create your views here.
class TrainListView(View):
    template_name = 'trains/trains_list.html'

    def get(self, request):
        trains = Train.objects.all()
        return render(request, self.template_name, {'trains': trains})

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
        
    # def form_invalid(self, form):
    #     # Handle the case when the form is invalid
    #     return self.render_to_response(self.get_context_data(form=form))

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # You can add additional context variables if needed
    #     return context
        
class NotFoundView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'not_found.html')