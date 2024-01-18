from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Review
from train.models import Train
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here
class TrainReviewView(LoginRequiredMixin, View):
    template_name = 'train_review.html'

    def get(self, request, train_id):
        train = get_object_or_404(Train, id=train_id)
        reviews = Review.objects.filter(train=train)
        return render(request, self.template_name, {'train': train, 'reviews': reviews})

    def post(self, request, train_id):
        train = get_object_or_404(Train, id=train_id)
        comment = request.POST.get('comment')
        user_review = Review(train=train, user=request.user, comment=comment)
        user_review.save()
        return HttpResponseRedirect(reverse('train_review', args=[train_id]))

class ContactUsView(View):
    template_name = 'contact_us.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Here, you can add your logic to handle the form data
        # For example, you can send an email, save to the database, etc.

        return HttpResponseRedirect(reverse('contact_us'))