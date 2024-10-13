
num=2
print("hola",num)
i=0
tex="4"
def dummy():
    global i
    print(i)
    i+=1
dummy()
dummy()
dummy()
print(int(tex)+num)
s="g"
try: # Comienzo del bloque try
    valorInt = int(s) # Se produce una excepción
    print('Es entero') # Esta línea no se ejecuta
except: # Comienzo del bloque except
    print('No es entero')
print('Hemos terminado')
