import requests
import csv
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import time  # For simulating delay

API_KEY = 'QU5aTHZaY2ZWdG5aQ2t3REdPSkJjVW0waU80dDRYbWlJOGdCZkIyRg=='
BASE_API_URL = 'https://api.countrystatecity.in/v1'

def index(request):
    return render(request, 'cityapp/index.html')

# Fetch states for India
def get_states(request):
    country_code = 'IN'  # Hardcoded for India
    headers = {'X-CSCAPI-KEY': API_KEY}
    states_url = f'{BASE_API_URL}/countries/{country_code}/states'
    response = requests.get(states_url, headers=headers)
    states = response.json()
    return JsonResponse(states, safe=False)

# Fetch cities and save to CSV
def fetch_cities(request):
    state_code = request.GET.get('state_code')
    country_code = 'IN'  # Hardcoded for India
    
    if not state_code:
        return JsonResponse({'error': 'Please select a state'}, status=400)

    headers = {'X-CSCAPI-KEY': API_KEY}

    # Get the selected state's name for including in the CSV
    states_url = f'{BASE_API_URL}/countries/{country_code}/states/{state_code}'
    state_response = requests.get(states_url, headers=headers)
    state_info = state_response.json()
    state_name = state_info['name']

    # Get cities of the selected state
    cities_url = f'{BASE_API_URL}/countries/{country_code}/states/{state_code}/cities'
    city_response = requests.get(cities_url, headers=headers)
    cities = city_response.json()
    
    # Prepare the CSV response with city names and state
    all_cities = [[city['name'], state_name] for city in cities]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="cities_of_{state_name}.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['City Name', 'State'])
    writer.writerows(all_cities)

    return response