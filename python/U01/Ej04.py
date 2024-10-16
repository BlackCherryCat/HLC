num = int(input("Inserte un numero \n"))
cero = False
pos = False
menorCien = False
par = False
if num % 2 == 0 & num != 0:
    par = True
elif num > 0:
    pos = True
elif num < 100 & num != 0:
    menorCien = True
else:
    cero = True
print("El número es cero: ", cero)
print("El número es positivo: ", pos)
print("El número es es menor que 100: ", menorCien)
print("El número es par: ", par)
