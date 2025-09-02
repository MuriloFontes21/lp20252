'''
Exercícios sobre os comandos de condição em python
'''
from datetime import date, datetime
HOJE = datetime.now()

def exemploSe():
    idade = int(input('Idade:'))
    if idade >= 18:
        print('Maior de idade')

def exemploSeSenao():
    idade = int(input('Idade:'))
    if idade >= 18:
        print('Maior de idade')    
    else:
        print('Menor de idade')
    print('fim do programa')

def exemploSe_SenaoSe_Senao():
    idade = int(input('Idade:'))
    if idade < 18:
        print('Menor de idade')    
    elif idade < 65:
        print('Maior de idade')
    elif idade < 50:
        print('Pessoa madura')
    else:
        print('Idoso')
    print('fim do programa')

#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.
def q2():
 n1 = int(input("Digite um número inteiro: "))
 n2 = int(input("Digite um número inteiro: ")) 
 x = n1 + n2
 if x > 10:
     print(f"{n1} + {n2} = {x}")


#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.
def q3():
 n1 = int(input("Digite um número: "))
 n2 = int(input("Digite um número: "))
 soma = n1 + n2

 if soma > 20:
     print(f"{soma} + 8 = ", soma + 8)
 if soma <= 20:
     print(f"{soma} - 5 = ", soma - 5)
#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".

def q3():
 num = int(input("Digite um número: "))

 if num % 3 == 0:
    print(f"{num} é múltiplo de 3.")
 else:
    print(f"{num} não é múltiplo de 3.")

#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.
def q4():
 n1 = int(input("Digite um número: "))

 if n1 % 5 == 0:
     print(f"{n1} é divisivel por 5.")
 else:
     print(f"{n1} não é divisel por 5.")

#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.

def q5():
 num = int(input("Insira um número: "))

 if num % 3 == 0 and num % 7 == 0:
     print(f"{num} é divisivel por 3 e 7.")
 else:
     print(f"{num} não é divisel por 3 e 7")

#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.

def q6():
 salario = float(input("Informe o salário: "))
 prestacao = float(input("Informe a prestação: "))

 sal = salario * 0.3

 if salario <= prestacao:
     print(":::::::::::::::::::::::::O empréstimo pode ser consedido.:::::::::::::::::::::::::")
 else:
     print(":::::::::::::::::::::::::O empréstimo não pode ser concedido:::::::::::::::::::::::::")

#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.
def q7():
 num = int(input('Informe um número: '))

 if num >= 20 and num <= 50:
     print(f':::::::::::::::::::::::::{num} está entre 20 e 50:::::::::::::::::::::::::')
 else:
     print(f'::::::::{num} não está entre 20 e 50::::::::')

#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".

num = int(input('Informe um número: '))

if num > 20:
   print('::::::::Maior do que 20::::::::')

elif num == 20:
   print('::::::::Igual a 20::::::::')
else:
   print('::::::::Menor que 20::::::::')

#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.

def q9():
 ano_nasc = int(input('Informe o ano de nascimento: '))
 ano_atual = int (input('Informe o ano atual: '))

 idade = ano_atual - ano_nasc
 print('A idade é : ', idade)

#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.
def q10():
 num1 = int(input("Digite o primeiro número: "))
 num2 = int(input("Digite o segundo número: "))
 num3 = int(input("Digite o terceiro número: "))

 if num1 <= num2 and num1 <= num3:
     if num2 <= num3:
         print(num1, num2, num3)
     else:
         print(num1, num3, num2)
 elif num2 <= num1 and num2 <= num3:
     if num1 <= num3:
         print(num2, num1, num3)
     else:
         print(num2, num3, num1)
 else:
     if num1 <= num2:
         print(num3, num1, num2)
     else:
         print(num3, num2, num1)


#11. Faça um programa que leia 3 números e imprima o maior deles.
def q11():
 n1 = int(input('Informe um número: '))
 n2 = int(input('Informe mais um número: '))
 n3 = int(input('Informe mais um número: '))

 if n1 > n2 and n1 > n3:
     print('O maior número é: ', n1)
 elif n2 > n1 and n2 > n3:
     print('O maior número é: ', n2)
 else:
     print('O maior número é: ', n3)
#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idade
#• Se é maior de 65 anos
def q12():
 idade = int(input('Idade:'))
 if idade < 18:
         print('Menor de idade')    
 elif idade < 65:
         print('Maior de idade')
 else:
         print('Idoso')

#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).

def q13():
 nome = str(input("Digite o nome: "))
 nota1 = float(input("Digite a primeira nota: "))
 nota2 = float(input("Digite a nota 2: "))

 medianota = (nota1 + nota2) /2

 if medianota >= 7:
     print(f'{nome} nota na prova 1 --> {nota1} e nota na prova 2 --> {nota2} a média foi de --> {medianota} e está aprovado.')
 elif medianota < 3:
     print(f'{nome} nota na prova 1 --> {nota1} e nota na prova 2 --> {nota2} a média foi de --> {medianota} e está reprovado.')
 else:
     print(f'{nome} nota na prova 1 --> {nota1} e nota na prova 2 --> {nota2} a média foi de --> {medianota} e está de prova final.')

#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%

salario = float(input('Informe o salário: '))

if salario <= 600:
   print('Isento de imposto.')

elif salario <= 1200:
    desconto = salario * 0.20
    print(f"Desconto do INSS (20%): R$ {desconto: }")
elif salario <= 2000:
    desconto = salario * 0.25
    print(f"Desconto do INSS (25%): R$ {desconto: }")
else:
    desconto = salario * 0.30
    print(f"Desconto do INSS (30%): R$ {desconto: }")

#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.

valor_compra = float(input("Digite o valor de compra do produto: R$ "))

if valor_compra < 20.00:
    lucro = valor_compra * 0.45
else:
    lucro = valor_compra * 0.30

valor_venda = valor_compra + lucro

print(f"Valor de venda: R$ {valor_venda: }")

#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos

idade = int(input("Digite a idade do nadador: "))


if 5 <= idade <= 7:
    categoria = "Infantil A"
elif 8 <= idade <= 10:
    categoria = "Infantil B"
elif 11 <= idade <= 13:
    categoria = "Juvenil A"
elif 14 <= idade <= 17:
    categoria = "Juvenil B"
elif idade >= 18:
    categoria = "Sênior"
else:
    categoria = "Sem categoria (idade abaixo da mínima permitida)"

print(f"Categoria: {categoria}")

#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00

nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idade da pessoa: "))

if idade <= 10:
    valor = 30.00
elif idade <= 29:
    valor = 60.00
elif idade <= 45:
    valor = 120.00
elif idade <= 59:
    valor = 150.00
elif idade <= 65:
    valor = 250.00
else:
    valor = 400.00

print(f"{nome} deverá pagar R$ {valor: } pelo plano de saúde.")

#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.

numero = int(input("Digite um número de 1 a 12: "))

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

if 1 <= numero <= 12:
    print(f"Mês correspondente: {meses[numero - 1]}")
else:
    print("Não existe mês com este número.")

#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".

p1 = int(input("Digite os pontos do jogador 1: "))
p2 = int(input("Digite os pontos do jogador 2: "))
p3 = int(input("Digite os pontos do jogador 3: "))

pontos = [p1, p2, p3]

pontos.sort(reverse=True)

print("Pontos em ordem decrescente:", pontos)

soma = sum(pontos)

if soma > 100:
    media = soma / 3
    print(f"Equipe classificada. Média de pontos: {media: }")
else:
    print("Equipe desclassificada.")

#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio

saldo_medio = float(input("Digite o saldo médio do cliente: R$ "))

if saldo_medio <= 500:
    credito = 0
elif saldo_medio <= 1000:
    credito = saldo_medio * 0.30
elif saldo_medio <= 3000:
    credito = saldo_medio * 0.40
else:
    credito = saldo_medio * 0.50

print(f"Saldo médio: R$ {saldo_medio: }")
print(f"Crédito especial concedido: R$ {credito: }")

#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:

nome_livro = input("Digite o nome do livro: ")

tipo_usuario = input("Digite o tipo de usuário (professor/aluno): ").strip().lower()

if tipo_usuario == "professor":
    dias = 10
elif tipo_usuario == "aluno":
    dias = 3
else:
    print("Tipo de usuário inválido. Use 'professor' ou 'aluno'.")
    exit()

print("\n--- Recibo de Empréstimo ---")
print(f"Nome do livro: {nome_livro}")
print(f"Tipo de usuário: {tipo_usuario.capitalize()}")
print(f"Total de dias para devolução: {dias} dias")

#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.

# Entrada do percurso
percurso = float(input("Digite o percurso em quilômetros: "))

tipo_carro = input("Digite o tipo do carro (A, B ou C): ").strip().upper()

if tipo_carro == "A":
    consumo = percurso / 12
elif tipo_carro == "B":
    consumo = percurso / 9
elif tipo_carro == "C":
    consumo = percurso / 8
else:
    print("Tipo de carro inválido. Use A, B ou C.")
    exit()

print(f"Consumo estimado de combustível: {consumo:.2f} litros")

#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano    180cal Abacaxi          75cal  Chá               20cal
#Peixe          230cal Sorvete diet     110cal Suco de laranja   70cal
#Frango         250cal Mousse diet      170cal Suco de melão     100cal
#Carne          350cal Mousse chocolate 200cal Refrigerante diet 65cal

print("Escolha o prato:")
print("1 - Vegetariano, 2 - Peixe, 3 - Frango, 4 - Carne")
prato = int(input("Opção do prato: "))

print("\nEscolha a sobremesa:")
print("1 - Abacaxi, 2 - Sorvete diet, 3 - Mousse diet, 4 - Mousse chocolate")
sobremesa = int(input("Opção da sobremesa: "))

print("\nEscolha a bebida:")
print("1 - Chá, 2 - Suco de laranja, 3 - Suco de melão, 4 - Refrigerante diet")
bebida = int(input("Opção da bebida: "))

# Validação e cálculo
if prato in pratos and sobremesa in sobremesas and bebida in bebidas:
    total_calorias = pratos[prato] + sobremesas[sobremesa] + bebidas[bebida]
    print(f"\nTotal de calorias da refeição: {total_calorias} cal")
else:
    print("\nOpção inválida! Verifique os números digitados.")

#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.

placa = input("Digite a placa do carro (ex: ABC1234): ").strip().upper()

digitos = ''.join(filter(str.isdigit, placa))

if digitos:
    ultimo_digito = digitos[-1]
    if ultimo_digito in meses:
        mes = meses[ultimo_digito]
        print(f"Mês de renovação do emplacamento: {mes}")
    else:
        print("Erro: Último dígito da placa inválido.")
else:
    print("Erro: Placa sem números válidos.")

#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos


indice = float(input("Digite o índice de poluição (ex: 0.3): "))

if indice <= 0.25:
    print("Índice dentro do aceitável. Nenhum grupo será intimado.")
elif 0.25 < indice <= 0.3:
    print("Atenção: 1º grupo de indústrias deve ser intimado.")
elif 0.3 < indice <= 0.4:
    print("Atenção: 1º e 2º grupos de indústrias devem ser intimados.")
elif 0.4 < indice <= 0.5:
    print("Atenção: 1º, 2º e 3º grupos de indústrias devem ser intimados.")
else:
    print("Índice crítico! Todos os grupos (1º, 2º e 3º) devem ser intimados imediatamente.")


def q91():
    data_str = input('Data de nascimento (dd/mm/aaaa): ')
    print(f'Ano atual: {date.time.strftime(HOJE, "%Y")}')
    data_nascimento = datetime.strptime(data_str, '%d/%m/%Y')
    if data_nascimento > Hoje:
        print('Data de nascimento inválida!')
    else:
        print(f'Idade: {int((HOJE - data_nascimento).days/365)} anos.')
