alunos = int(input("Numero de alunos: "))
i, soma = 0, 0

while i < alunos:
    soma += float(input(f"Nota do(a) Estudante Nº{i+1}: "))
    i+= 1
media = soma/alunos
print(f"Média da turma: {media}")