import requests
import csv


token = '648d70da-a1d2-3e97-b858-f61aa38c64f6'
id = 1
route = 'https://guiadigital.iaph.es/api/1.0/bien/inmueble/' + str(id)
headers = {'Authorization': 'Bearer ' + token}

fields = ['id', 'codigo', 'municipio', 'provincia', 'denominacion', 'caracterizacion', 'proteccion_s', 'tipologiaList']

r = requests.get(route, headers=headers, verify=False)

json_response = r.json() #this is a dict

for field in fields:
  if field in json_response:
    print(json_response[field])
