print('Seja bem vindo a Copiadora Luana e Cia') #Exibe uma mensagem de boas vindas com o meu nome, e logo em seguida, imprime os serviços disponiveis.
servD = ''' 
Escolha o serviço desejado
DIG - Digitalização
ICO - Impressão Colorida
IBO - Impressão Preto e Branco
FOT - Fotocópia 
'''
#Exibe os preços adicionais ao cliente
servicos_extras = ''' 
Serviços Adicionais
1 - Encadernação simples
2 - Encadernação de capa dura
0 - Sem serviço extra
'''
print(servD) # Demonstra os serviços disponiveis
# Define um dicionário com os preços dos serviços
precos_servicos = { 
'DIG': 1.10, # Preço do serviço de Digitalização 
'ICO': 1.00, # Preço do serviço de Impressão Colorida 
'IBO': 0.40, # Preço do serviço de Impressão Preto e Branco
'FOT': 0.20  # Preço do serviço de Fotocópia  
} 
# Define um dicionário com os preços dos serviços adicionais
precos_extras = { 
1: 15.00, # Preço da encadernação simples
2: 40.00, # Preço da encadernação de capa dura
0: 0.00  # Sem serviço adicional
} 
# Função para perguntar ao cliente qual serviço ele deseja
def escolha_servico(): 
 while True: # Loop infinito até que o usuário insira uma opção válida
    servico = input("Por favor, insira o serviço desejado (DIG/ICO/IBO/FOT): ") 
    if servico in precos_servicos: # Verifica se a opção inserida é válida
        return servico
        # Retorna a opção escolhida pelo usuário
    else: 
        print("Serviço inválido. Tente novamente.") # Imprime uma mensagem de erro se a opção não for válida
# Função para perguntar ao usuário quantas páginas eles querem e aplicar o desconto correspondente
def num_pagina():
    while True: # Loop infinito até que o usuário insira uma opção válida
        try: 
            num_pags = int(input("Por favor, insira o número de páginas: ")) # Pergunta ao usuário o número de páginas
            if num_pags < 20: # Se o número de páginas for menor que 20, não há desconto
                return num_pags
            elif num_pags < 200: # Se o número de páginas for entre 20 e 199, o desconto é de 15%
                return num_pags * 0.85
            elif num_pags < 2000: # Se o número de páginas for entre 1000 e 1999, o desconto é de 20%
                return num_pags * 0.8
            elif num_pags < 20000: # Se o número de páginas for entre 1000 e 19999, o desconto é de 25%
                return num_pags * 0.7
            else: 
                print("Não aceitamos pedidos com essa quantidade de páginas.") 
        except ValueError: 
            print("Número inválido. Tente novamente.") 
# Função para perguntar ao usuário quais serviços adicionais eles querem e calcular o custo total desses serviços
def servico_extra():
    total_extra = 0 # Inicializa o total de custos extras
# Loop que continua até que o usuário não queira mais nenhum serviço adicional
    while True: 
        print(servicos_extras) # Imprime os serviços adicionais disponíveis
# Tenta converter a entrada do usuário para um inteiro
        try: 
            extra = int(input("Por favor, insira o serviço adicional (1/2/0): "))
# Verifica se a entrada do usuário é um serviço adicional válido
            if extra in precos_extras: 
                total_extra += precos_extras[extra] # Adiciona o custo do serviço adicional ao total 
# Se o usuário inserir 0, isso significa que ele não quer mais nenhum serviço adicional
                return total_extra # Retorna o total de custos extras                
            else: 
                print("Serviço adicional inválido. Tente novamente.") # Imprime uma mensagem de erro se a entrada não for válida
        except ValueError: 
            print("Entrada inválida. Tente novamente.") # Imprime uma mensagem de erro se a entrada não puder ser convertida para um inteiro    
        

# Calcula o total a pagar com base no serviço, no número de páginas e nos serviços adicionais escolhidos pelo usuário
servico = escolha_servico() 
num_pags = num_pagina() 
extra = servico_extra() 
total = precos_servicos[servico] * num_pags + extra  
# Imprime o total a pagar pelo usuário
print("O total do seu pedido é: R$ {:.2f}".format(total))