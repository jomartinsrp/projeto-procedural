from modules.products import showProducts
from modules.cart import buyProducts, showCart, clearCart, totalValue
from modules.checkout import showPayMethods, choosePayMethod, clearPayCheck
from modules.extract import publishExtract, getItemsOnCart


menu = 0
while menu != 7:
  print(''''
    MENU DE OPÇÕES
    [1] VER PRODUTOS
    [2] COMPRAR PRODUTOS
    [3] VER CARRINHO
    [4] LIMPAR CARRINHO
    [5] FAZER PAGAMENTO
    [6] EXPORTAR PEDIDO
    [7] SAIR DA LOJA
    ''')

  menu = int(input('===== Olá, o que deseja fazer? '))

  if menu == 1:
    showProducts()

  elif menu == 2:
    showProducts()
    buyProducts()
    
  elif menu == 3:
    showCart()

  elif menu == 4:
    clearCart()
    clearPayCheck()

  elif menu == 5:
    showPayMethods()
    choosePayMethod()
    totalValue()

  elif menu == 6:
    getItemsOnCart()
    publishExtract()
    
  else:
    print('Digite uma opção válida, tente novamnente. ')

print('Volte sempre! ')