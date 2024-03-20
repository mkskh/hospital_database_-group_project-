from django.shortcuts import render
import requests


def index(request):

    if request.method == "GET":
        url = "http://127.0.0.1:8080/candidates/"

        response = requests.get(url).json()
        
        example = {"one": "two"}

        return render(request, 'candidates/index.html', {"response": response})
