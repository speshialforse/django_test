from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tutorials.models import Tutorial
from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import api_view

from django.http import HttpResponse
from django.template import loader
import json
from json import JSONEncoder
import requests

@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()
        print(tutorials)
        title = request.query_params.get('title', None)
        print(title)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        print(tutorials_serializer)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_200_OK)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try: 
        tutorial = Tutorial.objects.get(pk=pk) 
    except Tutorial.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = TutorialSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = Tutorial.objects.filter(published=True)
        
    if request.method == 'GET': 
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        x = {
            "name": "John",
            "age": 30,
            "city": "New York"
            }
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return JsonResponse(json.dumps(x), safe=False)
    
def members(request):
    mymembers = Tutorial.objects.all().values()
    template = loader.get_template('all_members.html')
    jsonmymembers = TutorialSerializer(mymembers, many=True)
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
        }
    
    contacts = {"xxx-xxx-xxxx": "Joe",
            "yyy-yyy-yyyy": "Joe",
            "zzz-zzz-zzzz": "Ane",
            "aaa-aaa-aaaa": "Rod",
            }

    apps = ["facebook",
            "linkedin",
            "twitter"]

    myMobile = MobilePhone(contacts, apps)
    jsonString = MobilePhoneEncoder().encode(myMobile)

    # convert into JSON:
    y = json.dumps(x)
    context = {
        'mymembers': mymembers,
        'jsonmymembers': jsonString,
    }
    return HttpResponse(template.render(context, request))

@api_view(['GET', 'POST', 'DELETE'])
def testjson(request):
    if request.method == 'GET':
        # tutorials = Tutorial.objects.all()
        # print(tutorials)
        # title = request.query_params.get('title', None)
        # print(title)
        # if title is not None:
        #     tutorials = tutorials.filter(title__icontains=title)
        
        # tutorials_serializer = TutorialSerializer(tutorials, many=True)
        # print(tutorials_serializer)
        resp = requests.post('https://httpbin.org/post', data={'website': 'datagy.io'})
        print(resp.text)
        return JsonResponse(json.loads(resp.text), safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        # tutorial_data = JSONParser().parse(request)
        # tutorial_serializer = TutorialSerializer(data=tutorial_data)
        # if tutorial_serializer.is_valid():
        #     tutorial_serializer.save()
        print(request)
        jsn = JSONParser().parse(request)
        jsn["modifed"] = "dgdfgdfg"
        newJson = {"jopa":"jopnaya","pizda":"nax","result": jsn["test"]}
        return JsonResponse(newJson, safe=False) 
        # return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        return JsonResponse({'test':'DELETE'}) 

# A class with JSON Serialization support

class MobilePhone:
    contacts = None
    apps = None

    def __init__(self, contacts, apps):
        self.contacts   = contacts
        self.apps       = apps

    def startCall():
        pass
 
    def endCall():
        pass
# A specialised JSONEncoder that encodes MobilePhone

# objects as JSON
class MobilePhoneEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, MobilePhone):
            return object.__dict__
        else:
            return json.JSONEncoder.default(self, object)