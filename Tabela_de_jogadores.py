# Crie um menu para o usuário colocar os valores do personagem no banco de dados.
# Este menu deve continuar aparecer sempre, podendo sair somente se ele selecionar para sair.

#importar o sqlite
import sqlite3

#conectando a tabela no vscode
conexao = sqlite3.connect('tabela_personagem')

#executando ação
cursor = conexao.cursor()

#Criando a tabela, o jogador deverá colocar seu nome, Classe e a arma de escolha
#cursor.execute('CREATE TABLE jogadores(id INT NOT NULL,Nome VARCHAR(100),Classe VARCHAR(20), Arma VARCHAR(50));')

# Menu editar, com funções onde o usuário pode selecionar se quer editar o ID, nome, classe ou arma.
# Menu Excluir, usuário pode escolher exlcuir o seu usuário, ou seja, vai excluir todo o registro, incluindo Id, nome, Classe a arma.
# Menu Exibir, usuário pode selecionar escolher ver todos os usuário cadastrados, ver apenas, os dados de um usuário específico.
# Menu Exibir, usuário pode visualizar quais os jogadores estão cadastrados no banco, podendo visualizar seu nome.
# Menu Exibir, usuário pode visualizar qual a quantidade de jogadores utilizam cada arma cadastrada no banco, por exemplo se Isadora e Kenji utilizam espada,
# o resultado retornado deve ser dois jogadores utilizam espada, lembrando que o usuário vai digitar o que ele quer, e nao ter opções prontas.

def adicionar():
    respostaj = 's'    
    while respostaj == 's':
        id = input("Digite seu id: ")
        Nome = input("Digite seu Nome: ")
        Classe = input("Digite sua Classe: ")
        Arma = input("Digite a Arma de escolha: ")
        print(f'Adicionado com sucesso!\n')
        respostaj = str(input('Deseja adicionar mais personagens? [s/n]: '))
        dados = [id, Nome, Classe, Arma]
        sql_inserir = "INSERT INTO jogadores (id, Nome, Classe, Arma) VALUES (?, ?, ?, ?)"
        cursor.execute (sql_inserir, dados)
        if respostaj == 'n':
            menu()
    
def editar():
    respostaj = 's'    
    while respostaj == 's':
        resultado = cursor.execute('SELECT id, Nome, Classe, Arma FROM jogadores')
        for visualizar in resultado:
            print(visualizar)
        id = input("Digite o id do personagem a ser editado: ")
        Nome = input('Qual o novo nome do personagem? ')
        Classe = input('Qual a nova classe do personagem? ') 
        Arma = input('Qual a nova arma do personagem? ')
        print(f'Edição salva!\n')
        respostaj = str(input('Deseja editar mais algum personagem? [s/n]: '))
        dados = [Nome, Classe, Arma, id]
        sql_editar = "UPDATE jogadores SET Nome = ?, Classe = ?, Arma = ? WHERE id = ?"
        cursor.execute (sql_editar, dados)
        if respostaj == 'n':
            menu()

def excluir():
    respostaj = 's'    
    while respostaj == 's':
        resultado = cursor.execute('SELECT id, Nome, Classe, Arma FROM jogadores')
        for visualizar in resultado:
            print(visualizar)
        id = input('Digite o id a ser excluído: ')
        cursor.execute(f'DELETE FROM jogadores WHERE id = {id}')
        print(f'Registro excluído com sucesso!\n')
        respostaj = str(input('Deseja excluir mais algum personagem? [s/n]: '))
        if respostaj == 'n':
            menu()

def ver_jogadores():
    resultado = cursor.execute('SELECT id, Nome, Classe, Arma FROM jogadores')
    for visualizar in resultado:
        print(f'{visualizar}\n')
    menu()

def selecionar():
    respostaj = 's'
    while respostaj == 's':
        Arma = input('Digite a arma que você quer buscar: ')
        dados = [Arma]
        sql_armas = 'SELECT Arma FROM jogadores WHERE Arma = ?'
        resposta = cursor.execute(sql_armas, dados)
        contador = 0
        for arma in resposta:
            contador += 1
        print(f'Quantidade desta arma é: {contador}\n')
        respostaj = str(input('Deseja buscar mais alguma arma? [s/n]: '))
        if respostaj == 'n':
            menu()

def sair():
    print(f'Estamos finalizando seu programa!\n')
    conexao.commit()
    conexao.close
    exit

def menu():
    print(f'=================================\n')
    print('Escolha uma das opções digitando o número referente a ação desejada: ')
    print('Para adicionar jogador digite: 1')
    print('Para editar: 2')
    print('Para Excluir: 3')
    print('Para visualizar jogadores cadastrados: 4')
    print('Para selecionar um dos jogadores: 5')
    print('Para sair: 6')
    print(f'=================================\n')
    resposta = input('Digite uma das opções: ')

    if resposta == '1': #funcinou
        adicionar()
    elif resposta == '2': #funcinou
        editar()
    elif resposta =='3': #funcinou
        excluir ()
    elif resposta == '4': #funcinou
        ver_jogadores()
    elif resposta == '5': #funcinou
        selecionar()
    elif resposta =='6': #funcinou
        sair()
    else: #funcinou
        print('Resposta inválida!')

menu() #Chamando a função inicial menu