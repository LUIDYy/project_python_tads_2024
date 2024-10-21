#Discentes: Amanda Moreira Braz, Tony, Ellen ,Gabriel, Luidy Vieira.
#1 e 2 Período - TADS

import os
from random import randint
import math
#variaveis


print("//////// Seja Bem Vindo Aventureiro//////")

#Configurando o personagem
nome = str(input('Digite o nome do aventureiro: '))
classe=int(input("""Escolha Sua Classe :
                 [1]Guerreiro
                 [2]Arqueiro
                 [3]Clerico\n"""))



#mimik = baú surpresa
#random = 0, 20


#jogador = vida, esquiva, ataque, ataque crítico, defesa
jogador = [nome,5,0,3,0,1 ] 


#//////////ficha inicial ///////////

print('------STAUTUS------')
      
vida =5             
esquiva =0             
ataque =3
defesa =0            
ataque_critico =1 
if classe ==1:
    print("Voce escolheu a opcao Guerreiro") 
    ataque+=2
    defesa+=2
    print(f"vida={vida}\n")
    print(f"esquiva={esquiva}\n")
    print(f"ataque={ataque}\n")
    print(f"defesa={defesa}\n")
    print(f"ataque critico={ataque_critico}\n")
       
      
      
#Definição dos monstros -
monstroF = ['Fácil', , ,] #definir valores dos atributos dos monstros
monstroM = ['Médio', , ,]
monstroD = ['Difícil', , ,]
monstroB = ['Boss', , ,]

print(f'Bem-vindo à aventura, {jogador}.')

caverna = str(input('Deseja entrar na caverna misteriosa? [s/n]\n '))
if caverna == 's':
    print('Bem-vindo à Caverna. Pode entrar!')
else:
    print('Você saiu da caverna!🏃‍♂️💨')
    while True: