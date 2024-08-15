listalivro = []
id_global = 0

# Funçao principal para cadastrar e guardar os livros
def cadastrar_livro(id):
    global id_global # Variavel global para ser reutilizada
    id_global += 1
    nome = input("Escolha o nome do livro: ")
    autor = input("Escolha o nome do autor: ")
    editora = input("Escolha o nome da editora: ")
    livro = {"id": id, "nome": nome, "autor": autor, "editora": editora}
    listalivro.append(livro) # Guarda as informações fornecidas ao criar uma lista


def consultar_livro():
    while True:
        print("Consultar Livro:")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Autor")
        print("4. Retornar ao menu")
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:  # Opção para consulta completa dos livros cadastrados
            for livro in listalivro: # Consulta do item na variavel listalivro
                print(f"Livro: [ Nome: {livro['nome']} "
                      f"| ID: {livro['id']} "
                      f"| Autor: {livro['autor']} "
                      f"| Editora: {livro['editora']} ]\n")
                
        elif opcao == 2: # Pesquisa por ID de cadastro
            id_consulta = int(input("Digite o ID do livro desejado: "))
            for livro in listalivro:
                if livro['id'] == id_consulta:
                    print(f"Livro: [ Nome: {livro['nome']} "
                          f"| ID: {livro['id']} "
                          f"| Autor: {livro['autor']} "
                          f"| Editora: {livro['editora']} ]\n")
                    break
            else:
                print("Livro não encontrado.") # Imprime uma mensagem se a entrada não for válida
                break
        elif opcao == 3: # Opção para pesquisa pelo nome do autor
            autor_consulta = input("Digite o nome do autor desejado: ") #Solicita o nome do autor desejado.
            for livro in listalivro:
                if livro['autor'] == autor_consulta:
                    print(f"Livro: [ Nome: {livro['nome']} "
                          f"| ID: {livro['id']} "
                          f"| Autor: {livro['autor']} "
                          f"| Editora: {livro['editora']} ]\n")
        elif opcao == 4:
            break
        else:
            print("Opção inválida. Tente novamente") # Imprime uma mensagem de erro se a entrada não for válida
            continue

#Funçao para o usuario remover os livros.
def remover_livro():
    while True:
        id_livro_para_remover = int(input("Digite o ID do livro que quer remover ou digite 0 para voltar ao menu: ")) # Remover livro pela forma de pesquisa de ID da listalivro ou volta ao menu quando o usuario digita 0. 
        if id_livro_para_remover == 0:
            break
        for livro in listalivro:
            if livro['id'] == id_livro_para_remover:
                listalivro.remove(livro) # Utilizada a opção .remove na listalivro
                print("Livro '{}' removido.".format(livro['nome']))
                break
        else:
            print("ID inválido. Tente novamente") # Imprime uma mensagem de erro se a entrada não for válida
            continue


print("Bem vindo à livraria da Luana!") #Exibe uma mensagem de boas vindas com meu nome, em seguida, lista as opçoes disponiveis para o usuario.
while True:
    print("\nMenu Principal:")
    print("1 - Cadastrar Livro") 
    print("2 - Consultar Livro")
    print("3 - Remover Livro")
    print("4 - Encerrar Programa")
    escolha_menu_principal = int(input("Escolha uma opção: ")) #pergunta ao usuario a opçao desejada.

    if escolha_menu_principal == 1:
        print("")
        cadastrar_livro(id_global + 1)
    elif escolha_menu_principal == 2:
        print("")
        consultar_livro()
    elif escolha_menu_principal == 3:
        print("")
        remover_livro()
    elif escolha_menu_principal == 4:
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida.")
        continue


