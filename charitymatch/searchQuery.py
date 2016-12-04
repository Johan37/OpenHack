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
        if request.method == 'GET':
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

    # Filter on subjects selected
    matching_entries_category = filter_on_categories(search_param_dict, organisationList)
    matching_entries = matching_entries_category;

    # Filter on area selected
    matching_entries_area = filter_on_area(search_param_dict, organisationList)
    matching_entries = [org for org in matching_entries if org in matching_entries_area]

    # Filter on method selected
    matching_entries_method = filter_on_method(search_param_dict, organisationList)
    matching_entries = [org for org in matching_entries if org in matching_entries_method]

    # Send response with the ids filtered out
    filtered_ids = [obj.id for obj in matching_entries]
    return JsonResponse({"data": filtered_ids})

def filter_on_categories(search_param_dict, organisationList):
    # Retreive the subjects from parameters
    category_list = search_param_dict['subject']

    #If no category is selected, don't filter at all but send all the organisations
    if not category_list:
        return [org for org in organisationList]
    
    matching_entries_category = []
    for category in category_list:
        # Get a copy of a list of the organisations that match the current category
        current_matching_entires = [org for org in organisationList if category in get_organisation_parent_categories(org)]

        # Union it with the other filters' matches
        matching_entries_category = list(set(current_matching_entires).union(set(matching_entries_category)))

    return matching_entries_category

def filter_on_area(search_param_dict, organisationList):
    if 'area' not in search_param_dict:
        return [org for org in organisationList]

    # Get the chosen area
    picked_area = search_param_dict['area']
    print("picked area: {}".format(picked_area))
    
    # Get a copy of a list with the organisations that match the area
    matching_entires_area = [org for org in organisationList if picked_area in get_organisation_regions(org)]
    print('matching_entires_area: {}'.format(matching_entires_area))

    return matching_entires_area

def filter_on_method(search_param_dict, organisationList):
    if 'how' not in search_param_dict:
        return [org for org in organisationList]

    # Get the chosen method
    picked_method = search_param_dict['how']
    print("picked method: {}".format(picked_method))
    
    # Get a copy of a list with the organisations that match the method
    matching_entires_method = [org for org in organisationList if picked_method in get_organisation_methods(org)]
    print('matching_entires_method: {}'.format(matching_entires_method))

    return matching_entires_method
    
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

