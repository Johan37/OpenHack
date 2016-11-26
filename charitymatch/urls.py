from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'organization/(?P<organization_id>[0-9]+)', views.organization, name='organization'),
    # url(r'organization/<test_id>[0-9]+', views.organization, name='organization'),
    url(r'^$', views.index, name='index'),
]


