from django.views import View
from django.shortcuts import render

from people.models import Summary


class PeopleView(View): 
    
    def get(self, request):
        people_summaries  = []
        summaries = Summary.objects.all()
        for summar in summaries:
            if len(summar.summary_text) > 100:
                people_summaries.append(summar)
        people_summaries.sort(key=lambda s: s.updated_at, reverse=True)

        return render(request, 'people/people.html', {'people_reviews': people_summaries})
