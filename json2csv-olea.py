#!/usr/bin/python3
import csv
import json
import sys

files = sys.argv[1:]


with open('IAPH_import.csv', mode='w') as IAPH_import_file:
    csv_headers = ['id', 'codigo', 'denominacion', 'otros_nombres', 'tipo',
          'municipio', 'provincia', 'caracterizacion', 
          'crono_ini', 'crono_fin', 
          'denom_acti', 'den_tipologia', 'periodos', 'den_estilo',
          'proteccion_s', "latitud_s", "longitud_s"]
    writer = csv.DictWriter(IAPH_import_file, fieldnames=csv_headers)
    writer.writeheader()

    while files:
      print ("\n\nahora vamos con", files[0], "\n")
      with open( files[0] ) as f:
        data = json.load(f)
        registro_csv = {}
        registro_csv["id"] = data["id"]
        registro_csv["codigo"] = data["codigo"]
        registro_csv["denominacion"] = data["denominacion"]
        if "tipo_contenido" in data:
          registro_csv["tipo"] = data["tipo_contenido"]
        else :
          registro_csv["tipo"] = ""
        if "municipio" in data:
          registro_csv["municipio"] = data["municipio"]
        else :
          registro_csv["municipio"] = ""
        if "provincia" in data:
          registro_csv["provincia"] = data["provincia"]
        else:
          registro_csv["provincia"] = ""
        if "caracterizacion" in data:
          registro_csv["caracterizacion"] = data["caracterizacion"]
        else:
          registro_csv["caracterizacion"] = ""
        registro_csv["proteccion_s"] = data['proteccion_s']
        if "latitud_s" in data:
          registro_csv["latitud_s"] = data["latitud_s"]
        else:
          registro_csv["latitud_s"] = ""
        if "longitud_s" in data:
          registro_csv["longitud_s"] = data["longitud_s"]
        else:
          registro_csv["longitud_s"] = ""          
    


        try:
          denominacionList = []
          for x in data['denominacionList']['denominacion']:
            denominacionList.append(x["denominacion"])
        except:
          denominacionList =""

        try:
          tipologiaList = []        
          if isinstance(data["tipologiaList"]["tipologia"], dict):
            tipologiaList.append([ 
                data['tipologiaList']['tipologia']['crono_ini'],
                data['tipologiaList']['tipologia']['crono_fin'], 
                data['tipologiaList']['tipologia']['denom_acti'],
                data['tipologiaList']['tipologia']['den_tipologia'],
                data['tipologiaList']['tipologia']['periodos'],
                data['tipologiaList']['tipologia']['den_estilo']
            ]) 
          elif isinstance(data["tipologiaList"]["tipologia"], list):
            for idx, elm in enumerate(data["tipologiaList"]["tipologia"]):
              tipologiaList.append([ 
                data['tipologiaList']['tipologia'][idx]['crono_ini'],
                data['tipologiaList']['tipologia'][idx]['crono_fin'], 
                data['tipologiaList']['tipologia'][idx]['denom_acti'],
                data['tipologiaList']['tipologia'][idx]['den_tipologia'],
                data['tipologiaList']['tipologia'][idx]['periodos'],
                data['tipologiaList']['tipologia'][idx]['den_estilo']
              ])
        except:
          tipologiaList = ""

        writer.writerow({
          'id': registro_csv["id"],
          "codigo": registro_csv["codigo"],
          "denominacion": registro_csv["denominacion"],
          "tipo": registro_csv["tipo"],
          "municipio": registro_csv["municipio"],
          "provincia": registro_csv["provincia"],
          "caracterizacion": registro_csv["caracterizacion"],
          "proteccion_s": registro_csv["proteccion_s"],
          "latitud_s":  registro_csv["latitud_s"],
          "longitud_s": registro_csv["longitud_s"]
          })

        for value in tipologiaList: 
          writer.writerow({
            "crono_ini": value[0],
            "crono_fin": value[1],
            "denom_acti": value[2],
            "den_tipologia": value[3],
            "periodos": value[4],
            "den_estilo": value[5]
          })

        for idx in range(len(denominacionList)): 
          writer.writerow({
            "otros_nombres": denominacionList[idx],
          })

        f.close()
        print(files.pop(0), "procesado.")
