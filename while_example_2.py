import os
c =''
b=0;
while(1):
	print('Olá Mundo')
	print('Carregando:',b,'%')
	print('Carregando:',c)
	c='|'
	c=c*b
	b=b+1;
	a=b*10000;
	while(a>0):
		a=a-1;
	os.system('clear') or None