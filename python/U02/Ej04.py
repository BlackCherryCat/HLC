hora=int(input("Introduzca la hora de ahora \n"))
if hora>=6 and hora<=12:
    print("Buenos dias")
elif hora>=13 and hora<=20:
    print("Buenas tardes")
else:
    print("Buenas noches")