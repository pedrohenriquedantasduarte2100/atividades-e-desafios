inicio = int(input("digite o primeiro numero (inicio) "))

fim = int(input("digite o primeiro numero (fim) "))

if inicio <= fim:
    passo = 1
else:
    passo = -1
    
print(f"numeros no intervalo entre (inicio) e (fim): ")

for i in range(inicio, fim + passo, passo):
 print(f"{i}")
    