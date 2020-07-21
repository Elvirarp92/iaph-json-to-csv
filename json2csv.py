import requests
import csv

token = '648d70da-a1d2-3e97-b858-f61aa38c64f6'
id = 23525  # Casa de Pilatos
route = 'https://guiadigital.iaph.es/api/1.0/bien/inmueble/' + str(id)
headers = {'Authorization': 'Bearer ' + token}

r = requests.get(route, headers=headers, verify=False)

json_response = r.json()  # this is a dict

csv_headers = ['id', 'codigo', 'municipio', 'provincia',
               'denominacion', 'caracterizacion', 'proteccion_s',
               'crono_fin', 'crono_ini',
               'denom_acti', 'den_tipologia', 'periodos']

try:
    csv_file_name = json_response["codigo"] + ".csv"
    with open(csv_file_name, 'x') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_headers)
        writer.writeheader()
        if isinstance(json_response["tipologiaList"]["tipologia"], dict):
            writer.writerow({'id': json_response['id'], 'codigo': json_response['codigo'],
                             'municipio': json_response['municipio'], 'provincia': json_response['provincia'],
                             'denominacion': json_response['denominacion'], 'caracterizacion': json_response['caracterizacion'],
                             'proteccion_s': json_response['proteccion_s'],
                             'crono_fin': json_response['tipologiaList']['tipologia']['crono_fin'],
                             'crono_ini': json_response['tipologiaList']['tipologia']['crono_ini'],
                             'denom_acti': json_response['tipologiaList']['tipologia']['denom_acti'],
                             'den_tipologia': json_response['tipologiaList']['tipologia']['den_tipologia'],
                             'periodos': json_response['tipologiaList']['tipologia']['periodos']})
        elif isinstance(json_response["tipologiaList"]["tipologia"], list):
            for idx, elm in enumerate(json_response["tipologiaList"]["tipologia"]):
                writer.writerow({'id': json_response['id'], 'codigo': json_response['codigo'],
                                 'municipio': json_response['municipio'], 'provincia': json_response['provincia'],
                                 'denominacion': json_response['denominacion'], 'caracterizacion': json_response['caracterizacion'],
                                 'proteccion_s': json_response['proteccion_s'],
                                 'crono_fin': json_response['tipologiaList']['tipologia'][idx]['crono_fin'],
                                 'crono_ini': json_response['tipologiaList']['tipologia'][idx]['crono_ini'],
                                 'denom_acti': json_response['tipologiaList']['tipologia'][idx]['denom_acti'],
                                 'den_tipologia': json_response['tipologiaList']['tipologia'][idx]['den_tipologia'],
                                 'periodos': json_response['tipologiaList']['tipologia'][idx]['periodos']})
        print("Done!")

except IOError:
    print("I/O error!")
