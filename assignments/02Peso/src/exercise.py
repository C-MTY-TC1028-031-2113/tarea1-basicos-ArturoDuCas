def main():
    #escribe tu código abajo de esta línea
    peso0= float(input("Dame el peso inicial: "))
    peso1=float(input("Dame el peso final: "))
    meses=int(input("Dame la cantidad de meses: "))
    pormes= (peso0-peso1)/ meses
    print ("Lo que debes bajar por mes es: " + str(pormes))


if __name__ == '__main__':
    main()
