from django.shortcuts import render
from django.views import View
from .models import Train
from django.views.generic import FormView
from .forms import TrainSearchForm
from django.http import HttpResponse

# Create your views here.
class TrainListView(View):
    template_name = 'trains/trains_list.html'

    def get(self, request):
        trains = Train.objects.all()
        return render(request, self.template_name, {'trains': trains})
    
class TrainSearchView(FormView):
    template_name = 'index.html'
    form_class = TrainSearchForm
    success_url = 'search_train'

    def form_valid(self, form):
        from_station = form.cleaned_data['from_station']
        to_station = form.cleaned_data['to_station']
        date = form.cleaned_data['date']
        travel_class = form.cleaned_data['travel_class']

        # Filter the queryset based on the form data
        search_results = Train.objects.filter(
            from_station__iexact=from_station,
            to_station__iexact=to_station,
            date=date,
            travel_class__iexact=travel_class
        )

        context = {'search_results': search_results}
        return self.render_to_response(self.get_context_data(form=form, **context))

    def form_invalid(self, form):
        # Handle the case when the form is invalid
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add additional context variables if needed
        return context