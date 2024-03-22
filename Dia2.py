nombre = input("Dime tu nombre: ")
ventas = input("Dime tus ventas: ")

ventas = float(ventas)

comision = (ventas * 13)/100

comisionfinal=round(comision,2)

print(f"Hola {nombre} ganaste un total de {comisionfinal}")
