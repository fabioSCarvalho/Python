'''Ex048: Faça um programa que calcule a soma entre todos os números
que são múltiplos de três e que se encontram no intervalo de 1 até 500. '''
soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma = soma + n
        cont = cont + 1
print("Existem {} divididos por 3 e a soma deles é {} ".format(cont, soma))
