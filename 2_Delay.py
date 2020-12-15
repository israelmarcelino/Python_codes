'''
- EXEMPLO DE FUNÇÕES

def hello(meu_nome,idade):
   print('Olá',meu_nome,'\nSua idade é:',idade)
   
def calcular_pagamento(qtd_horas, valor_hora):
  horas = float(qtd_horas)
  taxa = float(valor_hora)
  if horas <= 40:
    salario=horas*taxa
  else:
    h_excd = horas - 40
    salario = 40*taxa+(h_excd*(1.5*taxa))
  return salario

from time import sleep
sleep(2)   
print("hello world")
Quando executo o código acima, há um atraso de cerca de dois segundos antes de “hello world” ser impresso.

'''
import os
from time import sleep

def time_delay(segundos):
    print('Em ',segundos,' segundos o programa irá finalizar.')
    sleep(segundos)   
    os.system('clear') or None

#APRESENTAÇÃO
print('**************************************')
print('**         APRENDENDO PYTHON        **')
print('**        Ambiente de acesso        **')
print('**   Designed by Israel Marcelino   **')
print('**      Date: 13/12/2021, 20h22     **')
print('**************************************')

time_delay(5)
