from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'organisation/(?P<organisation_id>[0-9]+)', views.organisation, name='organisation'),
    # url(r'organization/<test_id>[0-9]+', views.organization, name='organization'),
    url(r'^$', views.index, name='index'),
]


