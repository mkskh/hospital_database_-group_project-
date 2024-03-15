from django.shortcuts import render
from .consume_api import get_data


def index(request):
    return_data = get_data()
    print("API RETRIEVED", len(return_data))

    return render(request, 'employees/index.html', {'posts': return_data})
