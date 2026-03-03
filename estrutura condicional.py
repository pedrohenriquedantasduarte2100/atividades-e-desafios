idade = int(input("digite sua idade: "))

if (idade > 5) and (idade < 12):
    print("infantil")
    
elif (idade > 13) and (idade < 17):
    print("juvenil")
    
elif (idade > 18):
    print("adulto")
    
else:
    print("invalido idade menor que 5 anos")