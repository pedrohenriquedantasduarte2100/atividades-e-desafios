#Mesma atividade da 09, pórem mais simplificada 

salario = float(input("Qual o valor do seu salário? "))

if (salario > 0):
    if (salario <= 280):
        percentual = 20
    elif (salario <= 700):
        percentual = 15
    elif (salario <= 1500):
        percentual = 10
    else:
        percentual = 5
else:
    print("Insira um número válido!")

aumento = salario * (percentual / 100)
novo_salario = salario + aumento

print(f"Salário atual: {salario:.2f}")
print(f"Percentual aumentato: {percentual}%")
print(f"Valor do aumento: {aumento:.2f}")
print(f"Novo salário: {novo_salario:.2f}")