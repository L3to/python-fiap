n = int(input("Informe o número de alunos: "))
contador = 0
media = 0

while contador < n:
    nota = int(input("Informe a nota do aluno: "))
    contador += 1
    media += nota
    
media = media / n
print(f'A média da turma é {media}')
    