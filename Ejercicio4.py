print("EJERCICIO 4")
print("Con números de orden" )

tareas = [(2,"buscar información"),(1, "reunión" ),(4," patentar"), (3, "realizar presentación")]
print(f"Lista de tareas sin ordenar: {tareas}")

tareas.sort(key =lambda tareas: tareas[0],reverse=False )
print (f"lista de tareas ordenadas{tareas}")

print("Ordenar por orden alfabético pero sin número de orden")

tareas.sort(key =lambda tareas: tareas[1],reverse=False )
print (f"lista de tareas ordenadas por oeden alfabético {tareas}")
