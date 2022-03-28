from collections import deque

#Definir cola
canciones = deque()

#Agregar
canciones.append("Si veo a tu mamá")
canciones.append("La canción")
canciones.append("Yonaguni")
canciones.append("Baby oh")

#Editar
itemAReemplazar = 'Yonaguni'
nuevoValor = 'La Santa'
for index, item in enumerate(canciones):
        if item == itemAReemplazar:
            canciones[index] = nuevoValor

#Eliminar
canciones.pop()

#Mostrar
cancion_siguiente = canciones.pop()
print("Siguiente canción: " + cancion_siguiente) 

cancion_pasada = canciones.pop()
print("Canción sonando: " + cancion_pasada) 
