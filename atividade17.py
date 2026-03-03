continuar = 1
desconto = 5
valor_total = 0
preco=0
media = 0

quantidade = 0
while continuar != 0 :
    preço = float (input( "qual o preço do produto: "))
    while preço < 0 :
        print("valor invalido")
        print("")
        preço = float(input( "qual o preço do produto: "))

    valor_total += preço
    quantidade += 1
    continuar = float (input("deseja continuar: "))
    print("")
    media = valor_total / quantidade

pagamento = int(input("qual forma de pagamento: "))
print("")


if pagamento == 1:

    valor_total = valor_total - (valor_total * desconto / 100)

    print (f"valor total: {valor_total}")
    print("")
    print(f"quantidade de produtos: {quantidade}")
    print("")
    print(f"media de preço por produtos: {media}")

else:
    print (f"valor total: {valor_total}")
    print("")
    print (f"quantidade de produtos: {quantidade}")
    print("")
    print (f"media de preço por produtos: {media} ")