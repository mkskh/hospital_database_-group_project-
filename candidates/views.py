from django.shortcuts import render
import requests
from .forms import SearchForm

def index(request):

    url = "http://127.0.0.1:8080/candidates/"
    form = SearchForm(request.POST or None)

    if request.method == "GET":
        response = requests.get(url).json()
        return render(request, 'candidates/index.html', {"response": response, "form": form})
    
    if request.method == "POST" and form.is_valid():
        response = requests.get(url).json()
        key = form.cleaned_data['search']
        gender = form.cleaned_data['gender']
        age_more_than = form.cleaned_data['age_more_than']
        age_less_than = form.cleaned_data['age_less_than']

        search_res = []

        for item in response:
            if not key:
                search_res.append(item)
            else:
                match_found = False
                for field in item.values():
                    if str(key).lower() in str(field).lower():
                        search_res.append(item)
                        match_found = True
                        break
                if match_found:
                    continue 

        if gender:
            search_res = [item for item in search_res if item["gender"] == gender]

        if age_more_than:
            search_res = [item for item in search_res if item["age"] > age_more_than]

        if age_less_than:
            search_res = [item for item in search_res if item["age"] < age_less_than]

        return render(request, 'candidates/index.html', {"response": search_res, "form": form})


def reset(request):

    url = "http://127.0.0.1:8080/candidates/"
    form = SearchForm()

    response = requests.get(url).json()

    return render(request, 'candidates/index.html', {"response": response, "form": form})