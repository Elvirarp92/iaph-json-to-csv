import requests
import csv


token = '648d70da-a1d2-3e97-b858-f61aa38c64f6'
route = 'https://guiadigital.iaph.es/api/1.0/tesauro'
headers = {'Authorization': 'Bearer ' + token}

r = requests.get(route, headers=headers, verify=False)

json_response = r.json() #this is a dict
json_data = json_response['response']['docs'] #this is a list!


