import requests
import csv


token = '648d70da-a1d2-3e97-b858-f61aa38c64f6'
id = 1
route = 'https://guiadigital.iaph.es/api/1.0/bien/inmueble/' + str(id)
headers = {'Authorization': 'Bearer ' + token}

unique_fields = ['id', 'codigo', 'municipio', 'provincia',
                 'denominacion', 'caracterizacion', 'proteccion_s']
tipologia_fields = ['crono_fin', 'crono_ini',
                    'denom_acti', 'den_tipologia', 'periodos']
header_fields = unique_fields + tipologia_fields
csv_file_name = "File.csv"

r = requests.get(route, headers=headers, verify=False)

json_response = r.json()  # this is a dict
tipologia_list = json_response['tipologiaList']['tipologia']
data_row = {}

try:
    csv_file_name = json_response["codigo"] + ".csv"
    with open(csv_file_name, 'x') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header_fields)
        writer.writeheader()
        for field in unique_fields:
            if field in json_response:
                data_row[field] = json_response[field]
            else:
                data_row[field] = " "
        for field in tipologia_fields:
            if field in tipologia_list:
                data_row[field] = tipologia_list[field]
            else:
                data_row[field] = " "

        writer.writerow(data_row)
        print("Done!")

except IOError:
    print("I/O error!")
