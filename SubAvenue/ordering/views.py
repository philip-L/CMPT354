from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == "POST":
    	print(request.body)
    return HttpResponse(json.dumps({"shit": "it works"}))
