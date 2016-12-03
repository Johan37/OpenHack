from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Organisation

from random import shuffle


def index(request):

    organisations = list(Organisation.objects.order_by('name'))
    shuffle(organisations)

    template = loader.get_template('index.html')

    context = {
        'orgs': organisations,
    }

    return HttpResponse(template.render(context, request))


def organisation(request, organisation_id):

    organisation_local = get_object_or_404(Organisation, pk=organisation_id)
    template = loader.get_template('org.html')

    context = {
        'org': organisation_local,
    }  

    return HttpResponse(template.render(context, request))


def about(request):

    template = loader.get_template('about.html')
    context = {}
    return HttpResponse(template.render(context, request))
