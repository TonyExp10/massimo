#Calcolo valore massimo tra 10 numeri

i = 0
n= input ("Inserisci il 1° valore: ")
n= int(n)
m = n

while i < 9:
  n = input("Inserire un numero: ")
  n= int(n)
  if n>m:	
     m=n	
  i += 1

print ("Valore maggiore:"+ str(m))
 