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
          'proteccion_s', 
          "latitud_s", "longitud_s", 
          "prot_pagina", "prot_fecha", "prot_estado", "prot_numero", "prot_figura", 
          "prot_den_publica", "prot_tipologia",
          "partede_tipo", "partede_codigo", "partede_denominacion"]
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

        try:
          proteccionList = []        
          if isinstance(data["proteccionList"]["proteccion"], dict):
            proteccionList.append([ 
                data['proteccionList']['proteccion']['pagina'],
                data['proteccionList']['proteccion']['fecha'], 
                data['proteccionList']['proteccion']['estado'],
                data['proteccionList']['proteccion']['numero'],
                data['proteccionList']['proteccion']['figura'],
                data['proteccionList']['proteccion']['den_publica'],
                data['proteccionList']['proteccion']['tipologia']
            ]) 
          elif isinstance(data["proteccionList"]["proteccion"], list):
            for idx, elm in enumerate(data["proteccionList"]["proteccion"]):
              proteccionList.append([ 
                data['proteccionList']['proteccion'][idx]['pagina'],
                data['proteccionList']['proteccion'][idx]['fecha'], 
                data['proteccionList']['proteccion'][idx]['estado'],
                data['proteccionList']['proteccion'][idx]['numero'],
                data['proteccionList']['proteccion'][idx]['figura'],
                data['proteccionList']['proteccion'][idx]['den_publica'],
                data['proteccionList']['proteccion'][idx]['tipologia']
              ])
        except:
          proteccionList = ""

        try:
          codigoList = []        
          if isinstance(data["codigoList"]["codigo"], dict):
            codigoList.append([ 
                data['codigoList']['codigo']['tipo'],
                data['codigoList']['codigo']['codigo'], 
                data['codigoList']['codigo']['denominacion']
            ]) 
          elif isinstance(data["codigoList"]["codigo"], list):
            for idx, elm in enumerate(data["codigoList"]["codigo"]):
              codigoList.append([ 
                data['codigoList']['codigo'][idx]['tipo'],
                data['codigoList']['codigo'][idx]['codigo'], 
                data['codigoList']['codigo'][idx]['denominacion']
              ])
        except:
          codigoList = ""


        for idx in range(len(denominacionList)): 
          writer.writerow({
            "otros_nombres": denominacionList[idx],
          })

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

        for value in codigoList: 
          writer.writerow({
            "partede_tipo": value[0],
            "partede_codigo": value[1],
            "partede_denominacion": value[2]
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

        for value in proteccionList: 
          writer.writerow({
            "prot_pagina": value[0],
            "prot_fecha": value[1],
            "prot_estado": value[2],
            "prot_numero": value[3],
            "prot_figura": value[4],
            "prot_den_publica": value[5],
            "prot_tipologia": value[6]
          })


        f.close()
        print(files.pop(0), "procesado.")
