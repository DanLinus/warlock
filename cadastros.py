#!usr/bin/env python
# -*- coding: utf-8 -*- 
#Favor fazer um  cadastro antes de realizar uma consulta.
#se encontrar bugs, por favor reporte-os 
import time

def autor():
	print"Carregando..."
	time.sleep(0.5)
	print"Formatando....."
	time.sleep(1.5)
	
	print "\t\t!!! ESTE SISTEMA ESTÁ DESTINADO A USO DO TERESINA HACKER CLUBE"
	print "#"*80
	print "\t\tAutor:  DanLinus"
	print "\t\tE-mail: dandaodesign@gmail.com"
	print "\t\t Twitter:    @Danetworke"
	print "\t\tDon't Hacker to live, i'm live to Hacker"
	print "#"*80
	print "\n\n"
	a = raw_input("Deseja voltar para o menu inicial?(Y/N)").lower()
	
	if a == 'y':
		inicio()
	if a == 'n':
		print"Finalizando..."
		time.sleep(0.5)
		exit


def inicio ():
	
	print "Selecione uma das opcoes abaixo:\n"
        print "\t(1)Cadastro\t(2)Consulta\t(3)Sair \t(4)Sobre"
#	
        print "\n"
	escolha = input("Opcao ==|")


	if escolha == 1:
		cadastro()
	if escolha == 3:
		print"Finalizando..."
		time.sleep(0.5)
		exit
	if escolha == 2:
		ver()

	if escolha == 4:
		autor()
	
	if escolha >= 5:
		print("este numero nao esta no menu de opcoes")
		inicio()

	if escolha <= 0:
		print("este numero nao esta no menu de opcoes")
		inicio()

	
def cadastro ():

	arq = open("cadastro.txt", 'a')
        nome = raw_input("Entre com o nome do livro a ser cadastrado:\n==|")
        telr = raw_input("Entre com o Nome do Autor do Livro:\n==|")
        telc = raw_input("Entre com o Codigo de Barra:\n==|") 
	
	print "==============================================================="
	print "\tLIVROS CADASTRADOS!"
        print "Nome do Livro: %s\nAutor do Livro: %s\nCodido de Barra do Livro: %s\n" %(nome,telr,telc)
	print "==============================================================="
	aa = "%s\n%s\n%s\n" %(nome,telr,telc)
	arq.write(aa)
	arq.close()
	inicio()


def ver ():  
	
	print"(1)Visualizar Livros Cadastrados\t(2)Visualizar Nomes de Autores\t(3)Visualizar Tudo\t(4)Voltar para o inicio\t(5)Sair "
	
	escolha = input("Opcao ==|")
	
	if escolha == 1:
		print"="*30
		arq = open("cadastro.txt")
		ac = arq.readlines()
		for k in range(0, len(ac),3):
			print "=="*3
			print "Nome do Livro: %s\nAutor do Livro: %s" %(ac[k],ac[k+1])
		arq.close()
		print"="*30
		ver()
	
	
	if escolha == 2:
		print"="*30
		arq = open("cadastro.txt")
		ac = arq.readlines()
		for k in range(0, len(ac),3):
			print "=="*3
			print "Nome: %s\nTel.Cel: %s" %(ac[k],ac[k+2])
		arq.close()
		print"="*30
		ver()
	
	if escolha == 3:
	
		print"="*30
		arq = open("cadastro.txt")
		ac = arq.readlines()
		for k in range(0, len(ac),3):
			print "=="*3
			print "Nome: %s\nTel.Cel: %s\nTel.Res: %s" %(ac[k],ac[k+1],ac[k+2])
		arq.close()
		print"="*30
		ver()

	if escolha == 4:
		inicio()
	
	if escolha == 5:
		print"Finalizando..."
		time.sleep(0.5)
		exit
	
	if escolha <=0:
		print"="*30
		print("este numero nao esta no menu de opcoes")
		print"="*30
		ver()
	
	if escolha >=6:
		print"="*30
		print("este numero nao esta no menu de opcoes")
		print"="*30
		ver()
inicio()
