nome = input("Digite seu nome: ")
conceito = input("Digite qual o seu conceito: ")
match conceito:
    case "a"|"A":
        print(f"{nome}: Fortemente recomendado.")
    case "b"|"B"|"c"|"C":
        print(f"{nome}: Recomendado.")
    case "d"|"D":
        print(f"{nome}: Não recomendado.")

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso / altura ** 2
pesoMaximoNormal = 24 * altura ** 2
pesoMinimoNormal = 19 * altura ** 2
perderKg = peso - pesoMaximoNormal
ganharKg = pesoMinimoNormal - peso

print(f"Imc: {imc:.2f}")
if imc < 18.5:
    print("Baixo peso")
    print(f"Para atingir o imc normal é necessário ter {pesoMinimoNormal:.2f}kg \nou ganhar {ganharKg:.2f}kg")
elif imc >= 18.5 and imc < 25:
    print("Normal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
    print(f"Para atingir o imc normal é necessário ter {pesoMaximoNormal:2.f}kg \nou perder {perderKg:.2f}kg")
else:
    print("Obesidade")
    print(f"Para atingir o imc normal é necessário ter {pesoMaximoNormal}kg \nou perder {perderKg:.2f}kg")