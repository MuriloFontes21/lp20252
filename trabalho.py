import csv

ARQUIVO = "filmes.csv"

def carregarfilmes():
    filmes = []
    try:
        with open(ARQUIVO, newline='', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                filmes.append(linha)
    except FileNotFoundError:
        pass
    return filmes

def salvarfilmes(filmes):
    with open(ARQUIVO, 'w', newline='', encoding='utf-8') as f:
        campos = ['título', 'ano', 'gênero', 'avaliação']
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(filmes)

def listarfilmes(filmes):
    print("\n--- Filmes em catálogo ---")
    if not filmes:
        print("Nenhum filme cadastrado.\n")
    else:
        for f in filmes:
            print(f"{f['título']} ({f['ano']}) - {f['gênero']} - Avaliação: {f['avaliação']}")
        print()

def buscargenero(filmes):
    genero = input("Digite o gênero: ").strip().lower()
    encontrados = [f for f in filmes if f['gênero'].lower() == genero]
    print()
    if encontrados:
        for f in encontrados:
            print(f"{f['título']} ({f['ano']}) - Avaliação: {f['avaliação']}")
    else:
        print("Nenhum filme encontrado nesse gênero.")
    print()


def buscarano(filmes):
    ano = input("Digite o ano: ").strip()
    encontrados = [f for f in filmes if f['ano'] == ano]
    print()
    if encontrados:
        for f in encontrados:
            print(f"{f['título']} - {f['gênero']} - Avaliação: {f['avaliação']}")
    else:
        print("Nenhum filme encontrado nesse ano.")
    print()

def adicionarfilme(filmes):
    titulo = input("Título: ")
    ano = input("Ano: ")
    genero = input("Gênero: ")
    avaliacao = input("Avaliação 0 a 10: ")
    filmes.append({'título': titulo, 'ano': ano, 'gênero': genero, 'avaliação': avaliacao})
    salvarfilmes(filmes)
    print("O filme foi adicionado!\n")

def calcularmediaavaliacoes(filmes):
    if not filmes:
        print("Nenhum filme cadastrado.\n")
        return
    notas = [float(f['avaliação']) for f in filmes]
    media = sum(notas) / len(notas)
    print(f"Média das avaliações: {media:.2f}\n")

def menu():
    filmes = carregarfilmes()
    while True:
        print("""
        CATÁLOGO
1 - Listar todos os filmes
2 - Buscar por gênero
3 - Buscar por ano
4 - Adicionar novo filme
5 - Calcular média das avaliações
0 - Sair
""")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            listarfilmes(filmes)
        elif opcao == '2':
            buscargenero(filmes)
        elif opcao == '3':
            buscarano(filmes)
        elif opcao == '4':
            adicionarfilme(filmes)
        elif opcao == '5':
            calcularmediaavaliacoes(filmes)
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida.\n")

menu()
