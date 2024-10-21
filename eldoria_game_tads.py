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
      
Vida =5             
Equiva =0             
Ataque =3
Defesa =0            
Ataque_critico =1 
if classe ==1:
    print("")    
      
      
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