print("EJERCICIO 6")


def separador(lista_6):

  lista_6.sort()

  pares=[]
  impares=[]
  
  for i in lista_6:
    if (i %2 == 0):
      pares.append(i)
    else:
      impares.append(i)
      
  return pares
  return impares


pares,impares= separador([6,5,2,1,7])  
print(f"los númeors pares son :{pares}")
print(f"Los números impares son:{impares}")