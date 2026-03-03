def calcular_desconto(valor):
    if valor >= 500:
        desconto = 0.30
    elif valor >= 200:
        desconto = 0.20
    elif valor >= 100:
        desconto = 0.10
    else:
        desconto = 0.0

    valor_com_desconto = valor * (1 - desconto)
    return valor_com_desconto, desconto

valor_compra =float(input("Digite o valor da compra: R$ "))

valor_final, desconto_aplicado = calcular_desconto(valor_compra)

print(f"Seu desconto aplicado foi de: {int(desconto_aplicado * 100)}%")
print(f"De acordo com o desconto, seu valor final é: R$ {valor_final:.2f}")
