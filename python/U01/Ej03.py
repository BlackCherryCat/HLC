try:
    lado=int(input("Inserte cuanto mide el lado de la base \n"))
    altura=int(input("Inserte la altura \n"))
    base=lado*lado
    volumen=(base*altura)/3
    print("volumen: ",volumen)
    print("caben ",round(volumen/2500), " piscinas olimpicas")
except:
    print("introduce un numero valido")
