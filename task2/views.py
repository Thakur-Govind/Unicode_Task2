from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import time

# Create your views here.
def home(request):
    url= "https://api.spacexdata.com/v3/launches"
    response=requests.get(url)
    test=response.json()

    flights=[]
    for i in test:
        dict={}
        dict = {'FlightNumber': i['flight_number'], 'Rocket': i['rocket']['rocket_name'],'links': i['links']['mission_patch'], 'Time': time.strftime("%D %H:%M",time.localtime(i['launch_date_unix']))}
        flights.append(dict)
    print (flights)
    #return HttpResponse("<p><h4>{}</h4></p>".format(fl) for fl in flights)
    return render(request,'home.html',{'flight_list':flights})
