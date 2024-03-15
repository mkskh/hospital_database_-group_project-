from django.shortcuts import render
from .consume_api import get_data


# TODO add "gender" and "university"
# TODO creating proper form to display data
# TODO create categories like "profession" and "gender"
# TODO implement filter options
# TODO fetch potential errors (HTTPError, timeout, to many requests)
# TODO implement sorting of data (name, age, profession)

def index(request):
    return_data = get_data()
    print("API RETRIEVED", len(return_data))

    return render(request, 'employees/index.html', {'posts': return_data})
