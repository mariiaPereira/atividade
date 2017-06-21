# coding: utf-8
from estoque import cadastrar,vender,imprimir


class economizaTec:
 def menuPrincipal(self):
     cadastro = cadastrar()
     venda = vender()
     imprimi = imprimir()
     while True:
         print "==== Bem vindo(a) ao EconomizaTec====\n"
         print "Cadastrar um Produto: 1"
         print "Vender um Produto: 2"
         print "Imprimir Balanço: 3"
         print "Sair: 4"
         op = raw_input("\nOpcao: ")

         if op == "1":
             '''Cadastro dos produtos'''
             cadastro.cadastrarProduto()
         elif op == "2":
             '''Vender os produtos'''
             venda.venderProduto()
         elif op == "3":
             '''Imprimir Balanço'''
             imprimi.imprimirBalanco()
         elif op == "4":
             print "\nObrigado!\nVolte Sempre!"
             break
         else:
             print "\nOpcao Invalida!!!\n"
casa = economizaTec()
casa.menuPrincipal()