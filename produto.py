# coding: utf-8

class produto1:
 def __init__(self, nome, preco, tipo, estoque):
     self.nome = nome
     self.preco = preco
     self.tipo = tipo
     self.estoque = estoque
 def getNome(self):
     return self.nome
 def getPreco(self):
     return self.preco
 def getTipo(self):
     return self.tipo
 def getEstoque(self):
     return self.estoque

 def setEstoque(self,estoque2):
     self.estoque = estoque2