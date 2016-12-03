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

    # Retreive the input filters from request body
    search_param_dict = searchParameters['answers']
    print('Search parameters: {}'.format(search_param_dict))

    # Retreive a list of all organisations
    organisationList = list(Organisation.objects.all())

    # Retreive the subjects from parameters
    picked_subjects = search_param_dict['subject']

    matching_entries = []

    for subject in picked_subjects:
        # Get a copy of a list of the organisations that match the current subject
        current_matching_entires = [org for org in organisationList if subject in get_organisation_parent_categories(org)]

        # Union it with the other filters' matches
        matching_entries = list(set(current_matching_entires).union(set(matching_entries)))

    if 'area' in search_param_dict:
        # Get the chosen area
        picked_area = search_param_dict['area']
        print("picked area: {}".format(picked_area))
        
        #for org in organisationList:
            #print("org: {}".format(org))
            #print("org.regions: {}".format(org.regions))
            #print("org.regions.name: {}".format(org.regions.name))
            #print("list(org.regions.values_list(\"name\", flat=True)): {}".format(list(org.regions.values_list("name", flat=True))))
        
        # Get a copy of a list with the organisations that match the area
        matching_entires_area = [org for org in organisationList if picked_area in get_organisation_regions(org)]
        print('matching_entires_area: {}'.format(matching_entires_area))

        #Adjust the list of matches as the intersection with this list
        matching_entries = [org for org in matching_entries if org in matching_entires_area]
        print('Matching entires: {}'.format(matching_entries))

    if 'how' in search_param_dict:
        # Get the chosen method
        picked_method = search_param_dict['how']
        print("picked method: {}".format(picked_method))

        # Get a copy of a list with the organisations that match the method
        matching_entires_method = [org for org in organisationList if picked_method in get_organisation_methods(org)]

        #Adjust the list of matches as the intersection with this list
        matching_entries = [org for org in matching_entries if org in matching_entires_method]

    print('Matching entires: {}'.format(matching_entries))

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

def get_organisation_regions(org):
    return [region.lower() for region in list(org.regions.values_list("name", flat=True))]

def get_organisation_methods(org):
    return [method.lower() for method in list(org.methods.values_list("name", flat=True))]

