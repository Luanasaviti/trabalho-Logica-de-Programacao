#Boas vindas com meu nome.
nome = 'Luana' 
print(f'Seja bem-vindo a loja da {nome}!')

#Solicitando o valor do produto e a quantidade
valorp = float(input('Informe o valor unitário do produto escolhido: ')) 
qntd = int(input('Informe a quantidade do produto: '))

#Armazena o  valor total.
preco = valorp * qntd

#Validaçoes de menor, igual, maior (if e elif)
if preco < 2500:
  #desconto de 0%
  print(f'Valor da compra sem desconto é de: {preco}. ')
elif  (preco >= 2500 and  preco < 6000):
   #desconto de 4%
   desconto = preco * (4 / 100);
   precodesc = preco - desconto
   print(f'O valor da compra  sem desconto é de: {preco}')
   print(f'O valor com 4% de desconto é de: {precodesc}. ')

elif  preco >= 6000 and  preco < 10000:
   #desconto de 7%
   desconto = preco * (7 / 100)
   precodesc = preco - desconto
   print(f'O valor da compra  sem desconto é de: {preco}')
   print(f'O valor com 7% de desconto é de: {preco - precodesc}. ')
elif  preco >= 10000:
  #desconto de 11% 
  desconto = preco * (11 / 100)
  precodesc = preco - desconto
  print(f'O valor da compra  sem desconto é de: {preco}')
  print(f'O valor com 11% de desconto é de: {preco - precodesc}. ')



