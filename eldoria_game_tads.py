#Discentes: Amanda Moreira Braz, Tony, Ellen ,Gabriel, Luidy Vieira.
#1 e 2 Período - TADS

import os
from random import randint
import math

print("//////// Seja Bem Vindo Aventureiro//////")

#Configurando o personagem
nome = str(input('Digite o nome do aventureiro: '))

#mimik = baú surpresa
#random = 0, 20


#jogador = vida, esquiva, ataque, ataque crítico, defesa
jogador = [nome, , ,] #definir valores dos atributos

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