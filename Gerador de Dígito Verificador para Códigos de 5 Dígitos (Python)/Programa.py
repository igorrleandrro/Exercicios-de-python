formatados = []
def separardigitos(numero):
    string = []
    pesos = [6,5,4,3,2]
    digitos = []
    x=0
    string.append (int(numero))
    for i in numero:
        digitos.append(int(i))

    for i in numero:
        digitos[x] = digitos[x]*pesos[x]
        x+=1
    soma = sum(digitos)
    DV = soma%7
    string.append (DV)
    formatados.append (f'{numero}-{DV}')

numero=1
while numero != "0":
    numero = input('Digite um número de 5 dígitos ou 0 para encerrar o programa: ')
    if numero != "0":
        separados = separardigitos(numero)

for item in formatados:
    print (item)
