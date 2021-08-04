produtos = {}

def adiciona_produto(produto, valor):
    produtos[produto] = valor

def aplica_desconto(objeto):
    
    produtos[objeto] -= round(produtos[objeto] * 0.05, 2)              


adiciona_produto('macarrão', 10)
adiciona_produto('abobora', 25)
adiciona_produto('arroz', 50)
adiciona_produto('tomate', 5)
adiciona_produto('batata', 100)
print(produtos)
aplica_desconto('macarrão')
aplica_desconto('arroz')
print(produtos)
