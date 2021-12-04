# importar biblioteca que usa para mover e copiar
import shutil

# criar um método escrever arquivo
def escrever_arquivo(texto):

    # criando arquivo em uma pasta especifica
    # diretorio = 'C:/Projeto/globallabs/texte.txt'
    # arquivo = open(diretorio, 'w')
    
    # criar um arquivo
    arquivo = open('teste.txt', 'w') # o 'w' escreve
    # escrever no arquivo
    arquivo.write(texto)
    # fechar 
    arquivo.close()
#----------------------------------------------------------------
# criar um método atualizar arquivo
def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a') # o 'a' atualiza
    arquivo.write(texto)
    arquivo.close()
#----------------------------------------------------------------
# criar um método para ler o arquivo
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r') # o 'r' ler
    texto = arquivo.read()
    print(texto)
#----------------------------------------------------------------
# criar um método para manipular o arquivo
def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media
#----------------------------------------------------------------
# criar um método para copiar e mover o arquivo
def copia_arquivo(nome_arquivo):

    shutil.copy(nome_arquivo, 'C:/Users/alexw/Desktop/Python DIO/notas_alunos.txt')

def move_arquivo(nome_arquivo):

    shutil.move(nome_arquivo, 'C:/Users/alexw/Desktop/Python DIO/notas_alunos2.txt')


#----------------------------------------------------------------
if __name__ == '__main__':

    # move_arquivo('notas.txt')

    # copia_arquivo('notas.txt')

    # lista_media = media_notas('notas.txt')
    # print(lista_media)

    # escrever_arquivo('Primeira linha\n')
    # aluno = '\nMaria,10,9,10,6\n'

    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')