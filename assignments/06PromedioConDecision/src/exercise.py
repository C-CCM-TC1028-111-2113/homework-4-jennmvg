import math 

def main():
    #escribe tu código abajo de esta línea
contar=0
suma=0

while(True):
    nota=float(input("Nota: "))
    
    if nota<0:
        break
    contar= contar+1
    suma= suma+nota

promedio= suma/contar
print("Promedio:", promedio)

    pass
if __name__=='__main__':
    main()
