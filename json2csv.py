import json
import csv
import os

files = ["./json/ficha-inmueble-23525.jsonld"]

csv_headers = ['id', 'codigo', 'municipio', 'provincia',
               'denominacion', 'caracterizacion', 'proteccion_s',
               'crono_fin', 'crono_ini',
               'denom_acti', 'den_tipologia', 'periodos']

json_pathname = "./json"
json_directory = os.fsencode(json_pathname)

for file in os.listdir(json_directory):
    filename = os.fsdecode(file)
    if filename.endswith('.json') or filename.endswith('.jsonld'):
        csv_file_name = filename + "_IAPH_import.csv"
        try:
            with open(csv_file_name, 'x') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_headers)
                writer.writeheader()
                with open(os.path.join(json_pathname, filename)) as json_file:
                    data = json.load(json_file)
                    if isinstance(data["tipologiaList"]["tipologia"], dict):
                        writer.writerow({'id': data['id'], 'codigo': data['codigo'],
                                         'municipio': data['municipio'], 'provincia': data['provincia'],
                                         'denominacion': data['denominacion'], 'caracterizacion': data['caracterizacion'],
                                         'proteccion_s': data['proteccion_s'],
                                         'crono_fin': data['tipologiaList']['tipologia']['crono_fin'],
                                         'crono_ini': data['tipologiaList']['tipologia']['crono_ini'],
                                         'denom_acti': data['tipologiaList']['tipologia']['denom_acti'],
                                         'den_tipologia': data['tipologiaList']['tipologia']['den_tipologia'],
                                         'periodos': data['tipologiaList']['tipologia']['periodos']})
                    elif isinstance(data["tipologiaList"]["tipologia"], list):
                        for idx, elm in enumerate(data["tipologiaList"]["tipologia"]):
                            writer.writerow({'id': data['id'], 'codigo': data['codigo'],
                                             'municipio': data['municipio'], 'provincia': data['provincia'],
                                             'denominacion': data['denominacion'], 'caracterizacion': data['caracterizacion'],
                                             'proteccion_s': data['proteccion_s'],
                                             'crono_fin': data['tipologiaList']['tipologia'][idx]['crono_fin'],
                                             'crono_ini': data['tipologiaList']['tipologia'][idx]['crono_ini'],
                                             'denom_acti': data['tipologiaList']['tipologia'][idx]['denom_acti'],
                                             'den_tipologia': data['tipologiaList']['tipologia'][idx]['den_tipologia'],
                                             'periodos': data['tipologiaList']['tipologia'][idx]['periodos']})
            print("Done!")
        except IOError:
            print("I/O error!")
    else:
        continue

# try:
#     csv_file_name = "IAPH_import.csv"
#     with open(csv_file_name, 'x') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=csv_headers)
#         writer.writeheader()
#         with open(files[0]) as json_file:
#             data = json.load(json_file)
#             if isinstance(data["tipologiaList"]["tipologia"], dict):
#                 writer.writerow({'id': data['id'], 'codigo': data['codigo'],
#                                  'municipio': data['municipio'], 'provincia': data['provincia'],
#                                  'denominacion': data['denominacion'], 'caracterizacion': data['caracterizacion'],
#                                  'proteccion_s': data['proteccion_s'],
#                                  'crono_fin': data['tipologiaList']['tipologia']['crono_fin'],
#                                  'crono_ini': data['tipologiaList']['tipologia']['crono_ini'],
#                                  'denom_acti': data['tipologiaList']['tipologia']['denom_acti'],
#                                  'den_tipologia': data['tipologiaList']['tipologia']['den_tipologia'],
#                                  'periodos': data['tipologiaList']['tipologia']['periodos']})
#             elif isinstance(data["tipologiaList"]["tipologia"], list):
#                 for idx, elm in enumerate(data["tipologiaList"]["tipologia"]):
#                     writer.writerow({'id': data['id'], 'codigo': data['codigo'],
#                                      'municipio': data['municipio'], 'provincia': data['provincia'],
#                                      'denominacion': data['denominacion'], 'caracterizacion': data['caracterizacion'],
#                                      'proteccion_s': data['proteccion_s'],
#                                      'crono_fin': data['tipologiaList']['tipologia'][idx]['crono_fin'],
#                                      'crono_ini': data['tipologiaList']['tipologia'][idx]['crono_ini'],
#                                      'denom_acti': data['tipologiaList']['tipologia'][idx]['denom_acti'],
#                                      'den_tipologia': data['tipologiaList']['tipologia'][idx]['den_tipologia'],
#                                      'periodos': data['tipologiaList']['tipologia'][idx]['periodos']})
#             print("Done!")

# except IOError:
#     print("I/O error!")
