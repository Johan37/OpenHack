from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Organisation


def index(request):

    organisations = list(Organisation.objects.order_by('name'))
    template = loader.get_template('charitymatch/index.html')

    context = {
        'organisations': organisations,
    }

    return HttpResponse(template.render(context, request))


def organization(request, organization_id):

    return HttpResponse("Hej! {}".format(organization_id))
