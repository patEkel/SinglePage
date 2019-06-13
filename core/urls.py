from django.urls import path

from core.views import HomeView
from people.views import PeopleView
from books.views import BookView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('people/', PeopleView.as_view(), name='people'),
    path('books/', BookView.as_view(), name='books'),
]