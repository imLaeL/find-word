import os

string = str(input("Digite a string: "))

diretorio_corrente = str(input("Digite o caminho completo do diretório que deseja verificar: "))

arquivos_no_diretorio = [arquivo for arquivo in os.listdir(diretorio_corrente) if os.path.isfile(os.path.join(diretorio_corrente, arquivo))]

for arquivo in arquivos_no_diretorio:
    caminho_completo = os.path.join(diretorio_corrente, arquivo)

    with open(caminho_completo, 'r') as file:
        conteudo = file.read()

        if string in conteudo:
            print(f"A palavra '{string}' foi encontrada no arquivo: {caminho_completo}")
