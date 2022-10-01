print("EJERCICIO 5")

while True:
  numero_positivo = int(input("introduce un número positivo de máximo 4 dígitos:"))
  if numero_positivo < 0:
    print("El número debe ser positivo")
  else: 
    break

numero = str(numero_positivo )
if len (numero) >=4:
    print (f"{numero[-4]}000")
    print (f"{numero [-3]}00")
    print (f"{numero [-2]}0")
    print (f"{numero [-1]}")
elif len (numero) >= 3:
    print (f"{numero [-3]}00")
    print (f"{numero [-2]}0")
    print (f"{numero [-1]}")
elif len (numero) >= 2:
    print (f"{numero [-2]}0")
    print (f"{numero [-1]}")
elif len (numero) >= 1:
    print (f"{numero [-1]}")
else:
  print("Este número no es apto")