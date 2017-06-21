# coding: utf-8
from produto import produto1
listaproduto = []
total = 0.0


class cadastrar:
 def cadastrarProduto(self):

     while True:
         print "====Cadastros de Produtos====\n"
         nomeProduto = raw_input("Digite o nome do produto: ")
         precoProduto = float(raw_input("Digite o preço unitário do produto: "))
         if precoProduto <= 0:
             print "numero negativo é invalido"
             continue
         tipoProduto = raw_input("Digite o tipo do produto: ")
         estoqueProduto = int(raw_input("Digite a quantidade no estoque: "))

         existe = False
         if len(listaproduto) == 0:
             produ = produto1(nomeProduto, precoProduto, tipoProduto, estoqueProduto)
             listaproduto.append(produ)
             print "\n%i %s(s) cadastrado(s) com sucesso.\n" % (estoqueProduto, nomeProduto)
         else:
             for i in range(len(listaproduto)):
                 if listaproduto[i].getNome() == nomeProduto:
                     existe = True
                     print "Produto ja cadastrado"

             if existe == False:
                 produ = produto1(nomeProduto, precoProduto, tipoProduto, estoqueProduto)
                 listaproduto.append(produ)
                 print "\n%d %s cadastrado(s) com sucesso.\n"%(estoqueProduto,nomeProduto)


         op1 = raw_input("Deseja cadastrar outro produto? ")

         if op1.upper() == "SIM":
             continue
         elif op1.upper() == "NAO":
             break
         else:
             print "Invalido!"


'''----------------------------------------------------------------------------------------------------------------------------'''


class vender:
 def venderProduto(self):
     global total
     global restante
     while True:
         print "====Venda de Produtos====\n"
         nomeProduto = raw_input("Digite o nome do produto: ")
         existe = False
         for i in range(len(listaproduto)):
             if listaproduto[i].getNome() == nomeProduto:
                 existe = True
                 print "%s(%s): R$%.2f" % (listaproduto[i].getNome(), listaproduto[i].getTipo(), listaproduto[i].getPreco())
                 quantidade = int(raw_input("digite a quantidade que deseja vender: "))
                 if quantidade <= 0:
                     print("numero negativo é invalido")
                     continue
                 if listaproduto[i].getEstoque()>= quantidade:
                     listaproduto[i].setEstoque(listaproduto[i].getEstoque() - quantidade)
                     r = listaproduto[i].getPreco() * quantidade
                     total += r
                     print("total arrecadado: R$%.2f" % (r))
                 else:
                     print "Não é possível vender pois não há %s suficiente" %(nomeProduto)

         if existe == False:
             print "%s nao cadastrado no sistema" % (nomeProduto)
             break

         op = raw_input("Deseja vender outro Produto? ")
         if op.upper() == "SIM":
             continue
         elif op.upper() == "NAO":
             break
         else:
             print "Invalido"

'''------------------------------------------------------------------------------------------------------------------'''

class imprimir:
 def imprimirBalanco(self):
     total_arrecadado = 0.0
     print "==== Impressao de Balanco ====\n"
     print "Produtos cadastrados: \n"
     for i in range(len(listaproduto)):
         print "%d) %s(%s): R$%.2f" %(i+1,listaproduto[i].getNome(), listaproduto[i].getTipo(), listaproduto[i].getPreco())
         print"\tRestante: %d" %(listaproduto[i].getEstoque())
         total_arrecadado += listaproduto[i].getPreco() * listaproduto[i].getEstoque()
     print "Total arrecadado em vendas: R$%.2f\n" %(total)
     print "Total que pode ser arrecadado : R$ %.2f" %(total_arrecadado)

'''------------------------------------------------------------------------------------------------------------------'''

