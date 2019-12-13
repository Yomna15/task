from django.shortcuts import render

import requests
import json

URL = "https://maps.googleapis.com/maps/api/distancematrix/json"
API_KEY = "AIzaSyD1Ma-q4XP7nP7rr0Y9NRssq3i_I1n_iYo"

# ?units=imperial&origins=40.6655101,-73.89188969999998&destinations=40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626%7C40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626&key=YOUR_API_KEY"

def get_distance(request):
    if request.POST:
        api_request = URL + '?origins=' + request.POST['origin'] + '&destinations=' + request.POST['destination'] + '&key=' + API_KEY
        # api_request = URL + '?origins=Cairo&destinations=Alexandria&key=' + API_KEY
        
        response = requests.get(api_request)
        data = response.json()
        distance = 0
        for row in data['rows']:
            for element in row['elements']:
                distance = element['distance']['value']
        print(data)
        print(distance)
        return render(request,'api/api_form.html',{'distance':distance})
    return render(request,'api/api_form.html')

# get_distance("hi")