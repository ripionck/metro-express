from django.shortcuts import render
from django.views import View
from .models import Train

# Create your views here.
class TrainListView(View):
    template_name = 'trains/trains_list.html'

    def get(self, request):
        trains = Train.objects.all()
        return render(request, self.template_name, {'trains': trains})