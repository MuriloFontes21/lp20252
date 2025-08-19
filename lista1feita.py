'''
Exercícios sobre os comandos básicos em Python
'''

#1. Faça um programa que imprima o seu nome.
print("Murilo Fontes")

#2. Faça um programa que imprima o produto dos valores 30 e 27.
print(30 * 27)

#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
n1 = 5
n2 = 8
n3 = 12

media = (n1 + n2 + n3) / 3
print(media)

#4. Faça um programa que leia e imprima um número inteiro.
numero = int(input("Digite um número inteiro: "))
print("O nome digitado foi: ", numero)

#5. Faça um programa que leia dois números reais e os imprima.
n1 = int(input("Digite o primeiro numero inteiro: "))

n2 = int(input("Digite o segundo numero inteiro: "))

print("O primeiro número é: ", n1)
print("O segundo número é: ", n2)

#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
n = int(input("Digite um número: "))

antecessor = n - 1
sucessor = n + 1

print("O antecessor de", n, "é: ", antecessor)
print("O sucessor de", n, "é: ", sucessor)

#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.
nome = input("Digite o nome do cliente: ")
endereco = input("Digite o endereço do cliente: ")
telefone = input("Digite o telefone do cliente: ")

print("Nome:", nome)
print("Endereço:", endereco)
print("Telefone:", telefone)

#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

sub = n1 - n2
print("A subtração dos números é: ", sub)

#9. Faça um programa que leia um número real e imprima ¼ deste número.
num = float(input("Digite um número real: "))

calc = num / 4

print("O resultado é:", calc)

#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
n1 = float(input("Digite o primeiro número: "))

n2 = float(input("Digite o segundo número: "))

n3 = float(input("Digite o terceiro número: "))

calc =(n1 + n2 + n3) / 3

print("A média aritmética dos números digitados é: ", calc)

#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.
n1 = float(input("Digite o primeiro número: "))

n2 = float(input("Digite o segundo número: "))

adicao = n1 + n2
sub = n1 - n2 
mult = n1 * n2
div = n1 / n2

print("A adição é : ", adicao)
print("A subtração é: ", sub)
print("A multiplicação é: ", mult)
print("A divisão é: ",div)

#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.
n = float(input("Digite um número: "))

calc= n ** 2

print("O quadrado do número é:", calc)

#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.
saldo = float(input("Digite o saldo da conta poupança: "))

novosaldo = saldo * 1.02

print("O novo saldo, com reajuste de 2%, é:", novosaldo)

#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base*2 + altura*2) e a área (base * altura).    
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

perimetro = 2 * base + 2 * altura
area = base * altura

print("Perímetro do retângulo:", perimetro)
print("Área do retângulo:", area)

#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.

#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.

#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5

#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida em horas
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.
velocidade = int(input("Velocidade média em km/h: "))
tempo = float(input("Tempo de viagem em horas: "))

distancia = tempo * velocidade
consumocombustivel = distancia / 12

print("A distância percorrida é: ", distancia)
print("O consumo de combustivel foi de: ", consumocombustivel)

#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.
prestacao = float(input("Valor da prestação vencida R$:"))
taxajuros = float(input("Taxa de juros %: "))
periodoatraso = int(input("Periodo de atraso: "))

juros = prestacao * (taxajuros / 100) * periodoatraso
valorfinal = prestacao + juros

print(f"Valor da prestação vencida {prestacao}")
print(f"Periodo de atraso {periodoatraso}")
print("Valor a pagar: ", juros)
print("Valor total somado ao juros: ", valorfinal)
#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.