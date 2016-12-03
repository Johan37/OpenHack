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

    #Print the users search parameters. This is compared with organisation parameters
    print(searchParameters)

    #Get the data from the database
    #organisationList = list(Organisation.objects.filter(categories__contains=1).values("name", "categories", "countries"))
    #print(organisationList)


    #Calculate score per organisation

    #Send response with data
    return JsonResponse({"data": {}});










    #organisationList = Organisation.objects.values_list("name")
    #print(organisationList)

    #organisationList = Organisation.objects.all()
    #print(organisationList[0].name)