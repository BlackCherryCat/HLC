num = int(input("Introduzca número \n"))
esprimo = True
for i in range(2, num):
    if num % i == 0:
        esprimo = False
        break
if esprimo:
    print("Es primo")
else:
    print("No es primo")
