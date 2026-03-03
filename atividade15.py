salario = float(input("digite seu salario: "))

ano_atual = int(input("digite seu ano: "))

ano = 1996

porcentagem = 0.015


while ano <= ano_atual:
    
    salario = salario + (salario * porcentagem)
    
    porcentagem *=  2
        
    ano = ano + 1
    
print(f"seu salario atual é: {salario}")
