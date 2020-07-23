import json
import csv
import os
import sys

csv_headers = ['id', 'codigo', 'municipio', 'provincia',
               'denominacion', 'caracterizacion', 'proteccion_s',
               'crono_fin', 'crono_ini',
               'denom_acti', 'den_tipologia', 'periodos']

json_pathnames = sys.argv

for pathname in json_pathnames[1:]:
    json_directory = os.path.abspath(pathname)
    for file in os.listdir(json_directory):
        filename = os.fsdecode(file)
        if filename.endswith('.json') or filename.endswith('.jsonld'):
            csv_file_name = filename + "_IAPH_import.csv"
            try:
                with open(csv_file_name, 'x') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_headers)
                    writer.writeheader()
                    with open(os.path.join(pathname, filename)) as json_file:
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
