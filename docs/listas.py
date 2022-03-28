#Inicializar lista
superheroes = []

#Agregar
superheroes.append('Iron Man')
superheroes.append('Spiderman')
superheroes.append('Hulk')

#Editar
itemAReemplazar = 'Iron Man'
nuevoValor = 'Mark V'
for index, item in enumerate(superheroes):
        if item == itemAReemplazar:
            superheroes[index] = nuevoValor

#Eliminar
superheroes.pop(2)

#Mostrar
print('Mis superheroes favoritos: ')
for e in superheroes:
    print(e)