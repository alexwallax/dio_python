# criar um método escrever arquivo
def escrever_arquivo(texto):
    # criar um arquivo
    arquivo = open('teste.txt', 'w') # o 'w' escreve
    # escrever no arquivo
    arquivo.write(texto)
    # fechar 
    arquivo.close()

# criar um método atualizar arquivo
def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a') # o 'a' atualiza
    arquivo.write(texto)
    arquivo.close()

# criar um método para ler o arquivo
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r') # o 'r' ler
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    # escrever_arquivo('Primeira linha\n')
    # atualizar_arquivo('Terceira linha\n')
    ler_arquivo('teste.txt')