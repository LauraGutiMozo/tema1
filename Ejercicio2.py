print("EJERCICIO 2")
numero_magico =(12345679)
while True:
  numero_usuario = int(input("Escriba un número entre 1 y 9="))
  if numero_usuario <9:
    break
  else:
    print("No ha escrito un número menor que 9")

numero_usuario_mult = numero_usuario*9
numer_magico_final = numero_magico*numero_usuario_mult
print(f"Por arte de magia obtendremos:{numer_magico_final}")