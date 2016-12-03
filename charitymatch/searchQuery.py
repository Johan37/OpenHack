#For http response
import json
from django.http import JsonResponse

#Getting stuff from database
from django.db import models
from .models import Category, SubCategory, Organisation

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
    picked_subjects = search_param_dict['subject']
    # picked_subjects.append("Homless")
    print('Picked subjects: {}'.format(picked_subjects))

    #Picked_regions...?

    organisationList = list(Organisation.objects.all())

    matching_entries = []
    for subject in picked_subjects:

        # print("Subject: {}".format(subject))
        current_matching_entires = [org for org in organisationList if subject in get_organisation_parent_categories(org)]
        matching_entries = list(set(current_matching_entires).union(set(matching_entries)))

    # organisationCategories = list(Organisation.objects.values("categories"))

    print('Matching entires: {}'.format(matching_entries))


    # for org in organisationList:
    #     sub_categories = list(org.categories.all())
    #     for sub in sub_categories:
    #         print("Name: {}".format(sub.name))


    # Calculate score per organisation

    # Send response with data
    filtered_ids = [obj.id for obj in matching_entries]
    return JsonResponse({"data": filtered_ids})


def get_organisation_parent_categories(org):

    # Retrieve list with sub categories for organisation
    sub_categories = list(org.categories.all())

    # Retrieve matching parent categories for each sub category
    # ...and get lowercase
    parent_categories_redundant = [sub_category.category.name.lower() for sub_category in sub_categories]

    # Remove redundant parent categories
    parent_categories_unique = list(set(parent_categories_redundant))

    # print("Parent organisation category: {}".format(parent_categories_unique))

    return parent_categories_unique





        #organisationList = Organisation.objects.values_list("name")
    #print(organisationList)

    #organisationList = Organisation.objects.all()
    #print(organisationList[0].name)
