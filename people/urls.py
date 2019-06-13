
from django.conf.urls import url
from people.views import PeopleView


urlpatterns = [
	url(r'^$', PeopleView.as_view(), name='people'),
]
