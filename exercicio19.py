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