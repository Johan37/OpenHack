import json

from django.http import HttpResponse

def getSearchResults(request):
    #translate the JSON body to a Python Dictionary
    searchParameters = []
    if request.is_ajax():
        if request.method == 'POST':
            body_unicode = request.body.decode('utf-8')
            print('Raw Data: "%s"' % body_unicode)
            searchParameters = json.loads(body_unicode)
        else:
            return HttpResponse("Fail")
    else:
        return HttpResponse("Fail")
    print(searchParameters)


    return HttpResponse("OK");























"""
class searchParameters(object):
    def __init__(self):
        self.checkboxes = [[]]

    def __str__(self):
        return "Class searchParameters"

class questionAndAnswer(object):
    def __init__(self):
        self.question = ""
        self.score = -1
        self.important = False

    def __str__(self):
        return "q: " + self.question + ", s: " + self.score

def getSearchResult(searchParameters):

    return results

a = searchParameters()
print(a.checkboxes)
"""