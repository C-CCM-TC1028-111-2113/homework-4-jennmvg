import math

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

