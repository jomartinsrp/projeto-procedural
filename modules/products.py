



productsList = (
  {'id':1, 'produto':'RAÇÃO PARA GATOS', 'preco':29.00},
  {'id':2, 'produto':'COLEIRA PET', 'preco':40.00},
  {'id':3, 'produto':'POTE PLÁSTICO', 'preco':15.00},
  {'id':4, 'produto':'ROUPA CACHORRO', 'preco':99.00},
  {'id':5, 'produto':'ARRANHADOR', 'preco':299.00},
)

def showProducts():
  for p in productsList:
    print('ID: {} -- PRODUTO: {} -- PREÇO: R$ {}\n'.format(p['id'], p['produto'], p['preco']))