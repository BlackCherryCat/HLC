year = int(input("Introduce año \n"))
if year % 100 != 0 and year % 4 == 0 or year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("Sí")
else:
    print("No")
