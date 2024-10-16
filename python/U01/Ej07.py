nombre=input("Escriba su nombre ")
apellido1=input("Escriba su primer apellido ")
apellido2=input("Escriba su segundo apellido ")
nombreVal=False
if nombre.lower()[-1]==nombre.lower()[0]:
    nombreVal=True
if nombreVal==True & len(apellido1)==len(apellido2):
    print(nombre,apellido1,apellido2,"APTA")
else:
    print(nombre,apellido1,apellido2,"NO APTA")