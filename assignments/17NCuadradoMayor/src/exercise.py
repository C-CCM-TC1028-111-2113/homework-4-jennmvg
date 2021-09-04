import math

def main():
    #Escribe tu código debajo de esta línea

n= int(input("ingrese un número:"))

for numero in range (n):

    if numero%2==0:
        print("#")
    else: 
        print ("%")    
    pass

if __name__=='__main__':
    main()
