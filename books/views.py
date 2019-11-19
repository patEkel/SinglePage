from django.views import View
from django.shortcuts import render

from books.models import Review


class BookView(View): 
    
    def get(self, request):
        book_reviews  = []
        reviews = Review.objects.all()
        for br in reviews:
            if len(br.review_text) > 100:
                book_reviews.append(br)
        book_reviews.sort(key=lambda r: r.updated_at, reverse=True)

        return render(request, 'books/books.html', {'book_reviews': book_reviews})


