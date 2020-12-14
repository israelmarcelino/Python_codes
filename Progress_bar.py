
import time
import sys
import os
from time import sleep

def time_delay(segundos):
    print('Aguarde alguns segundos.')
    barra_de_progresso(segundos)
    os.system('clear') or None
    
def barra_de_progresso(tamanho):
 
    toolbar_width = tamanho*10; #Define o tamanho da barra
    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

    for i in range(toolbar_width):
        time.sleep(.1) # do real work here
        # update the bar
        sys.stdout.write("#")
        sys.stdout.flush()

    sys.stdout.write("]\n") # this ends the progress bar

password ='teste1234'

#APRESENTAÇÃO
print('**************************************')
print('**         APRENDENDO PYTHON        **')
print('**        Ambiente de acesso        **')
print('**   Designed by Israel Marcelino   **')
print('**      Date: 14/12/2020, 8h19      **')
print('**************************************')

#FUNÇÃO DE DELAY
time_delay(10)

# ENTRADA DO USUÁRIO
usuario = input('Insira seu nome: ')
print('Olá, ',usuario)
print('Aguarde...')

#FUNÇÃO DE DELAY
time_delay(3)

while(1):
    senha = input('Insira sua senha: ')
    os.system('clear') or None

    #VERIFICAÇÃO DA SENHA
    if(senha == password):
        print('\n\nACESSO AUTORIZADO. \nBem vindo ao Ambiente de Usuário.')
        break
    else:
        print('\n\nATENÇÃO! \nACESSO NEGADO. Tente novamente.')

        #FUNÇÃO DE DELAY
        time_delay(3)
