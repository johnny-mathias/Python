alunos = int(input("Numero de alunos: "))
i, soma, nota, vermelho, azul = 0, 0, 0, 0, 0

while i < alunos:
    nota = float(input(f"Nota do(a) Estudante Nº{i+1}: "))
    soma += nota
    if nota <= 5 and nota >= 0:
        vermelho += 1
    if nota > 5:
        azul += 1
    i+= 1
media = soma/alunos
print(f"Média da turma: {media}")
print(f"Alunos com nota vermelha: {vermelho}")
print(f"Alunos com nota azul: {azul}")