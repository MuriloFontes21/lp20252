velocidade = int(input("Velocidade média em km/h: "))
tempo = float(input("Tempo de viagem em horas: "))

distancia = tempo * velocidade
consumocombustivel = distancia / 12

print("A distância percorrida é: ", distancia)
print("O consumo de combustivel foi de: ", consumocombustivel)