import json

data = {}
data['Mercados'] = []

producto = ["Sony PlayStation 4 Slim 1TB Standard color negro azabache","Sony Playstation 4 Slim 1tb Standard Negro Open Box Nueva"]
precio = ["2.529.990","2.079.900"]

data['productos'].append({

        "producto" : str(producto[0]),
        "precio": str(precio[0])

                        })
data["productos"].append({

        "producto" : str(producto[1]),
        "precio": str(precio[1])

                        })

with open("datos_json.json", "w") as archivo_json:
        #escribimos y especificamos la identacion (4 espacios)
        json.dump(data, archivo_json, indent=4)