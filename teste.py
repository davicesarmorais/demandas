import json

with open("demandas.json") as file:
    demandas = json.load(file)

print(demandas["Demandas-concluidas"]["1098"]["datas"])

