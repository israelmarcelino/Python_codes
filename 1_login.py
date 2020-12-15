import os
password ='teste1234'

#APRESENTAÇÃO
print('**************************************')
print('**         APRENDENDO PYTHON        **')
print('**        Ambiente de acesso        **')
print('**   Designed by Israel Marcelino   **')
print('**      Date: 13/12/2021, 18h40     **')
print('**************************************')


#FUNÇÃO DE DELAY
a=10000000;
while(a>0):
	a=a-1;
os.system('clear') or None

# ENTRADA DO USUÁRIO
usuario = input('Insira seu nome: ')
print('Olá, ',usuario)
print('Aguarde...')

#FUNÇÃO DE DELAY
a=10000000;
while(a>0):
	a=a-1;
os.system('clear') or None

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
        a=10000000;
        while(a>0):
	        a=a-1;
        os.system('clear') or None
