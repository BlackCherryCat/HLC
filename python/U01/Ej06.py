try:
    num = int(input("Inserte un numero \n"))
    if num % 3 == 0:
        print("folios de color rojo: ", num // 3)
        print("folios de color verde: ", num // 3)
        print("folios de color azul : ", num // 3)
    if num % 3 == 2:
        print("folios de color rojo: ", (num // 3) + 1) 
        print("folios de color verde: ", (num // 3) + 1)
        print("folios de color azul : ", num // 3)
    if num % 3 == 1:
        print("folios de color rojo: ", (num // 3) + 1) 
        print("folios de color verde: ", num // 3)
        print("folios de color azul : ", num // 3)
except:
    print("No valido")  
