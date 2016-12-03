from django.conf.urls import url

from . import views
from . import searchQuery

urlpatterns = [
    url(r'organisation/(?P<organisation_id>[0-9]+)', views.organisation, name='organisation'),
    url(r'searchQuery', searchQuery.getSearchResults),
    # url(r'organization/<test_id>[0-9]+', views.organization, name='organization'),
    url(r'about/', views.about, name='about'),
    url(r'^$', views.index, name='index'),
]


