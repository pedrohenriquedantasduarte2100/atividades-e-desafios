aluno = input ("nome do aluno: ")

nota = 0

notas_lista = []

Tuplas = [aluno]

while nota < 10:
    nota = float(input("digite sua nota: "))
    
    if nota < 0:
        print("numero invalido")
        nota = float(input("digite sua nota novamente: "))
    
    print("se deseja continuar coloque um numero MAIOR que 10")
    
    notas_lista.append(nota)
    

