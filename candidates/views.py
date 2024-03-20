from django.shortcuts import render, redirect
from django.urls import reverse
import requests

from .forms import SearchForm


def index(request):

    if request.method == "GET":

        url = "http://127.0.0.1:8080/candidates/"
        form = SearchForm()

        response = requests.get(url).json()

        return render(request, 'candidates/index.html', {"response": response, "form": form})
    

    elif request.method == "POST":

        url = "http://127.0.0.1:8080/candidates/"
        form = SearchForm(request.POST)

        if form.is_valid():
            response = requests.get(url).json()
            key = form.cleaned_data['search']

            search_res = []

            if key:
                for item in response:
                    if key.lower() in item["first_name"].lower():
                        search_res.append(item)
                    elif key.lower() in item["last_name"].lower():
                        search_res.append(item)
                    elif key.lower() in item["city"].lower():
                        search_res.append(item)
                    elif key.lower() in item["email"].lower():
                        search_res.append(item)
                    elif key.lower() in item["phone"].lower():
                        search_res.append(item)
                    elif key.lower() in item["university"].lower():
                        search_res.append(item)
                    elif key.lower() in item["profession"].lower():
                        search_res.append(item)
                    
            return render(request, 'candidates/index.html', {"response": search_res, "form": form})


def reset(request):

    url = "http://127.0.0.1:8080/candidates/"
    form = SearchForm()

    response = requests.get(url).json()

    return render(request, 'candidates/index.html', {"response": response, "form": form})