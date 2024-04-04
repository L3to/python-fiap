n = int(input("Informe o número de alunos: "))
contador = 0
media = 0
while n <= 0:
    n = int(input("Valor inválido, digite novamente: "))
    
while contador < n:
    nota = float(input("Informe a nota do aluno: "))
    contador += 1
    media += nota
    
media = media / n
print(f'A média da turma é {media}')
    
