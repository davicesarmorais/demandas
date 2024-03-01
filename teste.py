import json

with open("demandas.json") as file:
    demandas = json.load(file)

print(demandas["Demandas-concluidas"]["1098"]["datas"])

if "4321" in demandas["Demandas-concluidas"] or "4321" in demandas["Demandas-ativas"]:
    print("Está em demandas")     
else:
    print("Nao esta em demandas")

print(demandas["4321"])