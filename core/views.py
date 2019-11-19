import random
from django.views import View
from django.shortcuts import render
from books.models import Review
from people.models import Summary


class HomeView(View): 
    
    def get(self, request):
        choice_pool = []
        book_reviews = Review.objects.all()
        people_summaries = Summary.objects.all()

        for b in book_reviews:
            if len(b.review_text) > 50:
                choice_pool.append(b)
        for p in people_summaries:
            if len(p.summary_text) > 50:
                choice_pool.append(p)

        ran = [random.choice(choice_pool)]
        val_type = "book"
        if type(ran[0]) == Summary:
            val_type = "summary"

        return render(request, 'core/home.html', {'val_type':val_type, 'review_or_summary': ran})
