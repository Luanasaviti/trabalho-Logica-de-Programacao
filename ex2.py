#Exibe uma mensagem de boas vindas com o meu nome, e logo em seguida, imprime o cardápio com os preços para os sabores de 'Açai´' e 'cupuaçu' de acordo com o seu tamanho.
print('Bem-vindo(a) a loja de Gelato da Luana')
print('-' * 15,'cardápio', '-' * 17)
print('-' * 42)
print('-' * 3,'|Tamanho| Cupuaçu (CP)| Açaí (AC) |---')
print('-' * 3,'|   P   | R$ 9,00     | R$ 11,00  |---' )
print('-' * 3,'|   M   | R$ 14,00    | R$ 16,00  |---' )
print('-' * 3,'|   G   | R$ 18,00    | R$ 20,00  |---' )

total = 0 
#loop infinito para permitir que o cliente repita o pedido. 
while True: 
    #Verifica se os sabores e os tamanhos sao validos.
    sabor = input('Digite o sabor desejado:(CP/AC) ')
    if sabor != 'CP' and sabor != 'AC': 
        #mensagem de erro se a entrada for diferente de 'CP' ou 'AC' para que o cliente possa tentar fazer o pedido novamente.
        print ('sabor invalido.Por favor, tente novamente')
        continue
    else:
       tamanho = input('Digite o tamanho desejado: ')
       if tamanho != 'P' and tamanho !='M' and tamanho !='G': 
          print ('tamanho invalido. tente novamente')
          continue
       #Se o sabor e o tamanho forem validos, é calculado o valor do pedido de acordo com as informaçoes do cardapio.
       else:
        if sabor =='CP':
          if tamanho =='P':
            preco = 9.00
            print(f'Voce pediu o tamanho p no valor de: {preco:.2f}')
          elif tamanho =='M':
            preco = 14.00
            print(f'Voce pediu o tamanho M no valor de: {preco:.2f}')
          else:
            preco = 18.00
            print(f'Voce pediu o tamanho G no valor de: {preco:.2f}')
        
        if sabor =='AC':
           if tamanho =='P':
             preco = 11.00
             print(f'Voce pediu o tamanho p no valor de: {preco:.2f}')
           elif tamanho =='M':
             preco = 16.00
             print(f'Voce pediu o tamanho M no valor de: {preco:.2f}')
           else: 
            preco = 20.00
            print(f'Voce pediu o tamanho G no valor de: {preco:.2f}')
    #Adiciona o preço do pedido ao total        
    total += preco
    #Pergunta para o cliente se deseja adicionar mais alguma coisa, retornando para as opcoes de sabores e tamanhos caso a resposta for 'S' e encerra se a resposta for 'N'.
    mais_pedidos = input('Deseja adicionar mais alguma coisa?(S/N)')
    if mais_pedidos != 'S':
      break
 #Informa para o cliente o valor total dos pedidos.   
print(f'O valor total é de {total:.2f}.')
            
       
    