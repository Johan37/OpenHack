import json

from django.http import JsonResponse

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
    print(searchParameters)

    #Get the data from the database

    #Calculate score per organisation

    #Send response with data
    return JsonResponse({"data": {}});
