import csv
from modules.cart import onCart
from modules.products import productsList

productName = []
productValue = []

productsOnCart = []

# def getItemsOnCart():
#   for i in onCart:
#     for produto in productsList:
#       if produto['id'] == i['id']:
#         productName = produto['produto']
#         productValue = produto['preco']
#         productsOnCart = productName, productValue
#         print(productsOnCart)
#       # return productsOnCart

def getItemsOnCart(id):
  for i in onCart:
    for produto in productsList:
      if produto['id'] == i['id']:
        productName = produto['produto']
        productValue = produto['preco']
        productsOnCart = productName, productValue
        print(productsOnCart)
        # return productsOnCart

print(map(getItemsOnCart, productsList))

def publishExtract():
  for i in productsOnCart:
    return i
  with open('venvprojetop/modules/files/extract.csv', 'w+') as ecsv:
    publish = csv.writer(ecsv, delimiter=',')
    publish.writerow(('nome', 'valor'))
    publish.writerow((i))
    