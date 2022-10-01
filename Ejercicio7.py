print("EJERCICIO 7")

def agregar_una_vez (lista_7):
  lista_7 = []
  
  for lis in lista_7:
    if lis == insertar:
      print("Error: Imposible añadir elementos duplicados ")
    else:
      lista_7.append (insertar)
      break

  return lista_7

insertar = input("que desea insertar en la lista?:")
lista_7 = agregar_una_vez (insertar)
print (lista_7)