alunos = int(input('digite o número de alunos: '))
lista = []
notageral = 0
num=0
acima = 0
abaixo = 0
aluno = 1
for i in range(alunos):
    nota = int(input(f'digite a nota do {aluno}º aluno: '))
    lista.append(nota)
    notageral += nota
    aluno += 1
media = notageral//alunos
print (f'A média dos alunos é {media}')

for x in range(alunos):
    if lista[num] >= media:
        acima = acima + 1
    if lista [num] < media:
        abaixo = abaixo + 1
    num = num + 1
print (f'{acima} alunos ficaram acima e {abaixo} abaixo da média')