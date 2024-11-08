def init():
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicación")
    print("4.División")
    print("5.Salir")
    op(input("Introduce una opcion 1-5 \n"))


def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multi(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


def op(opt):
    match(opt):
        case "1":
            try:
                num1 = float(input("Introduce un número \n"))
                num2 = float(input("Introduce otro número \n"))
                print("Resultado:", suma(num1, num2), "\n")
                init()
            except:
                print("Alguno de los números introducidos no son validos")
                op("1")
        case "2":
            try:
                num1 = float(input("Introduce un número \n"))
                num2 = float(input("Introduce otro número \n"))
                print("Resultado:", resta(num1, num2), "\n")
                init()
            except:
                print("Alguno de los números introducidos no son validos")
                op("2")
        case "3":
            try:
                num1 = float(input("Introduce un número \n"))
                num2 = float(input("Introduce otro número \n"))
                print("Resultado:", multi(num1, num2), "\n")
                init()
            except:
                print("Alguno de los números introducidos no son validos")
                op("3")
        case "4":
            try:
                num1 = float(input("Introduce un número \n"))
                num2 = float(input("Introduce otro número \n"))
                print("Resultado:", div(num1, num2), "\n")
                init()
            except:
                print("Alguno de los números introducidos no son validos")
                op("4")
        case "5":
            SystemExit
        case _:
            init()


init()
