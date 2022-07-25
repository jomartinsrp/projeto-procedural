



paymentMethods = (
  {'id':1,'formato':'Débito (5% em off)'},
  {'id':2,'formato':'Dinheiro (5% em off)'},
  {'id':3,'formato':'Cartão de Crédito'},
)

paymentCheck = []

def getPayMethodName():
  for name in paymentMethods:
    if name['id'] == id:
      return name['formato']

def showPayMethods():
  for p in paymentMethods:
    print('id: {} -- Forma de Pagamento: {}'.format(p['id'], p['formato']))

def choosePayMethod():
  id = int(input('Digite o ID do método de pagamento escolhido: '))
  paymentCheck.append({'id':id})
  print('Você escolheu pagar com: ')
  print(paymentCheck)

def clearPayCheck():
  for i in paymentCheck:
    paymentCheck.pop()