#!/usr/bin/python3
import csv
import json
import sys

files = sys.argv[1:]


with open('IAPH_import.csv', mode='w') as IAPH_import_file:
    # fieldnames = ['id', "codigo", "denominacion", "tipo",
    #     "municipio", "provincia", "caracterizacion",
    #     "crono_ini", "crono_fin", "periodos", "den_tipologia","denom_acti", "den_estilo"
    #   ]
    csv_headers = ['id', 'codigo', 'denominacion', 
          'municipio', 'provincia', 'caracterizacion', 
          'crono_ini', 'crono_fin', 
          'denom_acti', 'den_tipologia', 'periodos',
          'proteccion_s']
    writer = csv.DictWriter(IAPH_import_file, fieldnames=csv_headers)
    writer.writeheader()

    while files:
      print ("ahora vamos con", files[0], "\n")
      with open( files[0] ) as f:
        data = json.load(f)
        print (data["id"])

        # registro_csv = {}
        # registro_csv["id"] = data["id"]
        # registro_csv["codigo"] = data["codigo"]
        # registro_csv["denominacion"] = data["denominacion"]
        # if "tipo_contenido" in data:
        #   registro_csv["tipo"] = data["tipo_contenido"]
        # else :
        #   registro_csv["tipo"] = ""
        # if "municipio" in data:
        #   registro_csv["municipio"] = data["municipio"]
        # else :
        #   registro_csv["municipio"] = ""
        # if "provincia" in data:
        #   registro_csv["provincia"] = data["provincia"]
        # else:
        #   registro_csv["provincia"] = ""
        # if "caracterizacion" in data:
        #   registro_csv["caracterizacion"] = data["caracterizacion"]
        # else:
        #   registro_csv["caracterizacion"] = ""


        # writer.writerow({
        #   'id': registro_csv["id"],
        #   "codigo": registro_csv["codigo"],
        #   "denominacion": registro_csv["denominacion"],
        #   "tipo": registro_csv["tipo"],
        #   "municipio": registro_csv["municipio"],
        #   "provincia": registro_csv["provincia"],
        #   "caracterizacion": registro_csv["caracterizacion"],
        #   # "crono_ini": data["tipologiaList"]["tipologia"]["crono_ini"],
        #   # "crono_fin": data["tipologiaList"]["tipologia"]["crono_fin"],
        #   # "periodos": data["tipologiaList"]["tipologia"]["periodos"],
        #   # "den_tipologia": data["tipologiaList"]["tipologia"]["den_tipologia"],
        #   # "denom_acti": data["tipologiaList"]["tipologia"]["denom_acti"],
        #   # "den_estilo": data["tipologiaList"]["tipologia"]["den_estilo"]
        #   })

        if isinstance(data["tipologiaList"]["tipologia"], dict):
          writer.writerow({
            'id': data['id'], 
            'codigo': data['codigo'],
            'municipio': data['municipio'], 
            'provincia': data['provincia'],
            'denominacion': data['denominacion'],
            'caracterizacion': data['caracterizacion'],
            'proteccion_s': data['proteccion_s'],
            'crono_fin': data['tipologiaList']['tipologia']['crono_fin'],
            'crono_ini': data['tipologiaList']['tipologia']['crono_ini'],
            'denom_acti': data['tipologiaList']['tipologia']['denom_acti'],
            'den_tipologia': data['tipologiaList']['tipologia']['den_tipologia'],
            'periodos': data['tipologiaList']['tipologia']['periodos']})
        elif isinstance(data["tipologiaList"]["tipologia"], list):
          for idx, elm in enumerate(data["tipologiaList"]["tipologia"]):
              writer.writerow({
                'id': data['id'], 
                'codigo': data['codigo'],
                'municipio': data['municipio'], 
                'provincia': data['provincia'],
                'denominacion': data['denominacion'], 
                'caracterizacion': data['caracterizacion'],
                'proteccion_s': data['proteccion_s'],
                'crono_fin': data['tipologiaList']['tipologia'][idx]['crono_fin'],
                'crono_ini': data['tipologiaList']['tipologia'][idx]['crono_ini'],
                'denom_acti': data['tipologiaList']['tipologia'][idx]['denom_acti'],
                'den_tipologia': data['tipologiaList']['tipologia'][idx]['den_tipologia'],
                'periodos': data['tipologiaList']['tipologia'][idx]['periodos']})
                                                 
        f.close()
        print(files.pop(0))
