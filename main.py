import random,os

maior = 0
menor = 500
soma = 0
cont = 0
for i in range(500):
  n = random.randint(0,10000)
  print (n)
  soma = soma + n
  cont = cont + 1
  media = soma / cont
  if( n > maior):
      maior = n
  elif( n < menor):
      menor = n  
  
else:
  os.system('clear')
  print("Maior:",maior)
  print("Menor:",menor)
  print("Soma:",soma)
  print("Media",media)
    
    
  