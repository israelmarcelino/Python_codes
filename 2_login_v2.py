import time
import sys
import os
from time import sleep

def time_delay(segundos):
    toolbar_width = 30; #Tamanho da barra
    
    sys.stdout.write("\nCarregando [%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

    incremento = (segundos-1)/toolbar_width; #Mexe no tempo de incremento da barra
    
    for i in range(toolbar_width):
        time.sleep(incremento) # do real work here
        # update the bar
        sys.stdout.write("#")
        sys.stdout.flush()

    sys.stdout.write("]\n") # this ends the progress bar
    
    os.system('clear') or None
    
password ='teste1234'

#APRESENTAÇÃO
print('**************************************')
print('**         APRENDENDO PYTHON        **')
print('**        Ambiente de acesso        **')
print('**   Designed by Israel Marcelino   **')
print('**      Date: 14/12/2020, 8h19      **')
print('**************************************')

#FUNÇÃO DE DELAY
time_delay(3)

# ENTRADA DO USUÁRIO
usuario = input('Insira seu nome: ')
os.system('clear') or None
print('Olá, ',usuario)
print('Aguarde...')

#FUNÇÃO DE DELAY
time_delay(3)

while(1):
    senha = input('Insira sua senha: ')
    os.system('clear') or None

    #VERIFICAÇÃO DA SENHA
    if(senha == password):
        print('ACESSO AUTORIZADO. \nBem vindo ao Ambiente de Usuário.')
        time_delay(3)
        break
    else:
        print('ATENÇÃO! \nACESSO NEGADO. Tente novamente.')
        time_delay(3)
