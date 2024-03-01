import json

with open("demandas.json") as file:
    demandas = json.load(file)

print(demandas["1098"]["datas"])

if "4321" in demandas:
    print("Está em demandas")     
else:
    print("Nao esta em demandas")

numeros = []
titulos = []

for numero in demandas:
    numeros.append(numero)
    titulos.append(demandas[numero]["titulo"])

print(numeros)
print(titulos)

