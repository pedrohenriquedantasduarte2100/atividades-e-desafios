continuar = 1

produto = 0 

preco = 0 

Contador = 0

while continuar != 0 :
    
    produto = float(input("valor do produto: "))
    
    if produto == 0:
        break 
        print("valor invalido digite novamente")
        
    Contador += continuar
    
    preco += produto
    
    continuar = int(input("deseja continuar: "))
    
print(f"valor : {preco}")
print (f"quantidades compradas: {Contador} ")