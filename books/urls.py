from django.conf.urls import url
from books.views import BookView


urlpatterns = [
	url(r'^$', BookView.as_view(), name='books'),
]