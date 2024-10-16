numlargos = int(input("Inserte cantidad de largos \n"))
longpiscina = float(input("Inserte longitud de piscina \n"))
if numlargos % 2 == 0:
    print("Se han nadado", round((numlargos / 2) * longpiscina, 2), "metros a crol")
    print(round((numlargos / 2) * longpiscina, 2), "metros a espalda")
    print("un total de", (numlargos * longpiscina) / 100, "kilómetros")
else:
    print("Se han nadado", round(((numlargos / 2) + 0.5) * longpiscina, 2), "metros a crol")
    print(round(((numlargos / 2) - 0.5) * longpiscina, 2), "metros a espalda")
    print("un total de", (numlargos * longpiscina) / 100, "kilómetros")
