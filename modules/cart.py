from pydoc import getpager
from modules.products import productsList
from modules.checkout import paymentCheck
from functools import reduce

onCart = []

def getProductName(id):
  for name in productsList:
    if name['id'] == id:
      return name['produto']

def getPayMethod(id):
  for method in paymentCheck:
    if method['id'] == id:
      return method['id']

def buyProducts():
  id = int(input('Digite o ID do produto para adicionar ao carrinho: '))
  quantity = int(input('Digite a quantidade que deseja comprar: '))
  onCart.append({'id':id, 'quantidade':quantity})
  print(onCart)

def showCart():
  for i in onCart:
    sumCart = 0
    for produto in productsList:
      if produto['id'] == i['id']:
        sumCart = sumCart + (produto['preco'] * i['quantidade'])
        break
    print('Produto:{0} -- Quantidade: {1}'.format(getProductName(i['id']), i['quantidade']))
    print('Valor: R$ {}'.format(sumCart))

def clearCart():
  for i in onCart:
    print('Limpando o carrinho... ')
    onCart.pop()
    print('Seu carrinho está vazio! ')

def soma(x,y):
  return x + y

def totalValue():
  for v in onCart:
    valor = 0
    for produto in productsList:
      if produto['id'] == v['id']:
        valor = produto['preco'] * v['quantidade']
        break
    if getPayMethod(id=1):
      valor = valor - (valor * 5 / 100)
      print('O valor a ser pago é R$ {}'.format(valor))
    elif getPayMethod(id=2):
      valor = valor - (valor * 5 / 100)
      print('O valor a ser pago é R$ {}'.format(valor))
    else:
      print('O total a ser pago é de R$ {}'.format(valor))