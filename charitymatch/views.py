from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Organisation


def index(request):

    organisations = list(Organisation.objects.order_by('name'))
    template = loader.get_template('index.html')

    context = {
        'orgs': organisations,
    }

    return HttpResponse(template.render(context, request))


def organisation(request, organisation_id):

    organisation = get_object_or_404(Organisation, pk=organisation_id)
    template = loader.get_template('org.html')

    context = {
        'org': organisation,
    }  

    return HttpResponse(template.render(context, request))
