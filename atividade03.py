peso = float(input("Digite o seu peso (Kg): "))
estatura = float(input("Digite a sua estatura (metros): "))

imc = peso / (estatura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
else:
    print("Classificação: Sobrepeso/Obesidade")
