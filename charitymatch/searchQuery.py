#For http response
import json
from django.http import JsonResponse

#Getting stuff from database
from django.db import models
from .models import Category, SubCategory, Organisation, Question

def getSearchResults(request):

    #translate the JSON body to Python
    searchParameters = []
    if request.is_ajax():
        if request.method == 'POST':
            body_unicode = request.body.decode('utf-8')
            print('Raw Data: "%s"' % body_unicode)
            searchParameters = json.loads(body_unicode)
        else:
            return JsonResponse(status=500, data={'status':'false','message':"Internal error: wrong method type (method was " + request.method + ")"})
    else:
        return JsonResponse(status=500, data={'status':'false','message':"Internal error: The request is not ajax"})

    # Print the users search parameters. This is compared with organisation parameters
    print("Search params {}".format(searchParameters['answers']))

    search_param_dict = searchParameters['answers']


    organisationList = list(Organisation.objects.all())


    picked_subjects = search_param_dict['subject']
    picked_subjects.append('Homless')

    print('Picked subjects: {}'.format(picked_subjects))

    matching_entries = []
    for subject in picked_subjects:

        matching_entries = [org for org in organisationList if subject in list(org.categories.all())]



    print('Matching entires {}'.format(matching_entries))



    # for key in search_param_dict:
    #     print(search_param_dict[key])
    #
    #     picked_values_list = search_param_dict[key]










    # Get the data from the database

    # organisationList = list(Organisation.objects.values("name", "categories", "countries"))
    print(organisationList)

    organisationCategories = list(Organisation.objects.values("categories"))

    for org in organisationList:

        categories = list(org.categories.all())

        for sub in categories:
            print("Name: {}".format(sub.name))


    #Calculate score per organisation

    #Send response with data
    return JsonResponse({"data": {}});










    #organisationList = Organisation.objects.values_list("name")
    #print(organisationList)

    #organisationList = Organisation.objects.all()
    #print(organisationList[0].name)