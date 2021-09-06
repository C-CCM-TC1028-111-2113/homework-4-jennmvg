import math
def main():
    num = int(input("Escribe un numero : "))
    #escribe tu código abajo de esta línea
    while num>0:
        cuadrado= math.sqrt(num)
        print (math.ceil (cuadrado))
        break

    pass

if __name__ == '__main__':
    main()
