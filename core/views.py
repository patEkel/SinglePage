import random
from django.views import View
from django.shortcuts import render

from books.models import Review


class HomeView(View): 
    
    def get(self, request):
        reviews = Review.objects.all()
        ran = [random.choice(reviews)]
        return render(request, 'core/home.html', {'book_reviews': ran})
